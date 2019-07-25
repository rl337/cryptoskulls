import PIL.Image
import urllib2

class Collage(object):
    item_width = None
    item_height = None
    url = None

    im = None
    items_per_row = None
    items_per_col = None
    total_items = None

    def __init__(self, url, item_width=24, item_height=24):
        self.item_width = item_width
        self.item_height = item_height
        self.url = url

        fp = urllib2.urlopen(url)
        self.im = PIL.Image.open(fp)

        assert self.im.width % self.item_width == 0, "Item collage is an uneven number of items wide"
        assert self.im.height % self.item_height == 0, "Item collage is an uneven number of items tall"

        self.items_per_row = self.im.width / self.item_width
        self.items_per_col = self.im.height / self.item_height

        self.total_items = self.items_per_row * self.items_per_col

    def __del__(self):
        self.im.close()

    def get_by_id(self, id):
        n = int(id)
        assert n >= 0 and n < self.total_items, "Item id %d is not a valid item" % n

        x = n % self.items_per_row
        y = n / (self.items_per_row)

        x_coord = x * self.item_width
        y_coord = y * self.item_height

        item_im = self.im.copy()
        return item_im.crop( (x_coord, y_coord, x_coord + self.item_width, y_coord + self.item_height))
