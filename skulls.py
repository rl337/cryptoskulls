import argparse
import cryptoskulls.images
import cryptoskulls.skulls
import cryptoskulls.colors.wikipedia
import json


def show_skull(url, id):
    collage = cryptoskulls.images.Collage(url)
    skull_im = collage.get_by_id(id)
    skull_im.show()


def import_wikipedia_colors():
    colors = cryptoskulls.colors.wikipedia.import_wikipedia_colors()
    print json.dumps(colors, indent=4)


def show_collage_colors(url):
    collage = cryptoskulls.images.Collage(url)
    colors = collage.list_colors()
    colors.sort()
    for color in colors:
        print color


def print_features(url, id):
    collage = cryptoskulls.images.Collage(url)
    skull_im = collage.get_by_id(id)
    skull = cryptoskulls.skulls.Skull(skull_im)

    print "Nose: %s" % skull.nose

parser = argparse.ArgumentParser(description='Perform an action on a Crypto Skull')
parser.add_argument('--url', metavar='url', type=str, default='https://cryptoskulls.com/images/cryptoskulls.png')
parser.add_argument('--id', metavar='id', type=int, default=None)
parser.add_argument('command', metavar='CMD', type=str)

args = parser.parse_args()

if args.command == 'colors':
    show_collage_colors(args.url)

if args.command == 'show':
    assert args.id is not None, "show command requires --id"
    show_skull(args.url, args.id)

if args.command == 'features':
    assert args.id is not None, "features command requires --id"
    print_features(args.url, args.id)

if args.command == 'import_wikipedia_colors':
    import_wikipedia_colors()
