import cryptoskulls.skulls
from cryptoskulls.colors import X, R, G, B, O, S, K

import PIL.Image
import PIL.ImageDraw

import unittest


def new_image(pixels):
    wid = len(pixels[0])
    height = len(pixels)

    im = PIL.Image.new('RGBA', (wid, height))
    draw = PIL.ImageDraw.ImageDraw(im)
    for x in range(wid):
        for y in range(height):
            draw.point((x, y), pixels[y][x])

    return im

test_skull_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, B, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, B, B, B, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, B, B, B, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, K, K, B, B, B, B, K, K, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, K, O, O, B, B, B, B, O, O, K, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, K, O, O, O, O, B, B, O, O, O, O, K, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, K, O, O, O, O, O, O, O, O, O, O, K, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, O, O, O, O, O, O, O, O, O, O, O, O, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, O, O, K, K, O, O, O, O, K, K, O, O, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, O, O, K, K, K, O, O, K, K, K, O, O, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, O, O, K, R, K, O, O, K, R, K, O, O, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, O, O, K, K, K, O, O, K, K, K, O, O, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, K, K, O, O, O, O, K, K, O, O, O, O, K, K, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, K, O, O, O, O, K, K, O, O, O, O, K, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, K, K, K, O, O, O, O, O, O, K, K, K, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, K, O, O, O, O, O, O, K, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, K, O, O, O, O, K, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, K, O, O, K, O, O, K, O, O, K, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, S, K, O, O, K, K, O, O, K, S, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, S, S, K, O, O, O, O, K, S, S, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, S, S, S, K, K, K, K, S, S, S, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, S, S, S, S, S, S, S, S, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, S, S, S, S, S, S, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, S, S, S, S, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

test_cases = [
    {
        'name': '',
        'image': test_skull_1,
        'assert': lambda s: s.nose is not None
    },
]


class CryptoskullsSkullsSkullTests(unittest.TestCase):

    def test_features(self):
        for test_case in test_cases:
            im = new_image(test_case['image'])
            im.show()
            skull = cryptoskulls.skulls.Skull(im)
            self.assertTrue(test_case['assert'](skull), "%s failed" % test_case['name'])
