import argparse
import cryptoskulls.images


def show_skull(url, id):
    collage = cryptoskulls.images.Collage(url)
    skull = collage.get_by_id(id)
    skull.show()

parser = argparse.ArgumentParser(description='Perform an action on a Crypto Skull')
parser.add_argument('--url', metavar='url', type=str, default='https://cryptoskulls.com/images/cryptoskulls.png')
parser.add_argument('--id', metavar='id', type=int, required=True)
parser.add_argument('command', metavar='CMD', type=str)

args = parser.parse_args()
if args.command == 'show':
    show_skull(args.url, args.id)
