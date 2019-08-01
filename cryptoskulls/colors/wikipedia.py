import urllib2
import HTMLParser

from cryptoskulls.colors import split_rgba


class WikiPageParser(HTMLParser.HTMLParser):
    tag_stack = None
    current_color = None
    colors = None

    def __init__(self, colors):
        HTMLParser.HTMLParser.__init__(self)
        self.tag_stack = []
        self.colors = colors

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append((tag, attrs))

    def handle_endtag(self, tag):
        self.tag_stack.pop()

    def tag_path(self):
        return [x[0] for x in self.tag_stack]

    def handle_data(self, data):
        if len(self.tag_stack) < 3:
            return

        tag_path = self.tag_path()
        if tag_path[-4:] == ['tbody', 'tr', 'th', 'a']:
            uri = None
            attrs = self.tag_stack[-1][1]
            for attr in attrs:
                if attr[0] == 'href':
                    uri = attr[1]
                    break
            self.current_color = [ data.strip(), uri ]
        elif tag_path[-3:] == ['tbody', 'tr', 'th']:
            pass
        elif tag_path[-2:] == ['tbody', 'tr']:
            pass
        elif tag_path[-3:] == ['tbody', 'tr', 'td']:
            if self.current_color is not None:
                self.current_color.append(data.strip())
        else:
            self.current_color = None

        if self.current_color is not None and len(self.current_color) > 2:
            if self.current_color[2].startswith('#'):
                color_data = {
                    'name': self.current_color[0],
                    'wiki': "https://en.wikipedia.org%s" % self.current_color[1],
                    'rgb': split_rgba(self.current_color[2])
                }
                if color_data not in self.colors:
                    self.colors.append(color_data)


wikipedia_color_urls = [
    "https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F",
    "https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M",
    "https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z",
]


def import_wikipedia_colors():
    colors = []
    for url in wikipedia_color_urls:
        parser = WikiPageParser(colors)
        fp = urllib2.urlopen(url)

        encoding = fp.headers['content-type'].split('charset=')[-1]

        for line in fp:
            uline = unicode(line, encoding)
            parser.feed(uline)
        fp.close()
    return colors
