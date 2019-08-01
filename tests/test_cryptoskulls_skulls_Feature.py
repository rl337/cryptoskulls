import cryptoskulls.skulls
from cryptoskulls.colors import X, R, G, B, K

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


test_cases = [
    {
        'name': 'Feature without color should pass',
        'feature': [
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]
        ],
        'image': [
            [X, X, X],
            [K, X, K],
            [X, X, X]
        ],
        'assert': lambda f, i: f.present(i)
    },
    {
        'name': 'Colors outside of feature should pass',
        'feature': [
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]
        ],
        'image': [
            [R, G, B],
            [K, G, K],
            [R, G, B]
        ],
        'assert': lambda f, i: f.present(i)
    },
    {
        'name': 'Colors inside uncolored feature should fail',
        'feature': [
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]
        ],
        'image': [
            [X, X, X],
            [B, X, B],
            [X, X, X]
        ],
        'assert': lambda f, i: not f.present(i)
    }
]


class CryptoskullsSkullsFeatureTests(unittest.TestCase):

    def test_features(self):
        for test_case in test_cases:
            im = new_image(test_case['image'])
            feature = cryptoskulls.skulls.Feature(test_case['feature'])
            self.assertTrue(
                test_case['assert'](feature, im),
                "%s failed" % test_case['name']
            )
