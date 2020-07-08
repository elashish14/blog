from itertools import product

import numpy as np
from scipy import interpolate

CHAR_MAPPING = np.array(list(
    '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
))
MAX_WIDTH = 627

def read_image(fh):
    metadata = next(fh).split()[4]
    width, height = map(int, metadata.split(',')[:2])
    image = np.zeros((width, height, 3)) # FIXME hardcoded number of channels
    for line in fh:
        fields = line.split()
        w, h = map(int, fields[0].strip(':').split(','))
        rgb = fields[1][1:-1].split(',')
        image[w, h, :] = list(map(int, rgb))
    return image

def rgb_to_brightness(image):
    return .21 * image[:,:,0] + .72 * image[:, :, 1] + .07 * image[:, :, 2]

def scale_image(image):
    num_in_cols, num_in_rows, channels = image.shape
    in_cols = np.linspace(0, 1, num_in_cols)
    in_rows = np.linspace(0, 1, num_in_rows)
    out_cols = np.linspace(0, 1, MAX_WIDTH)
    num_out_rows = out_cols.size * num_in_rows // (num_in_cols * 3)
    out_rows = np.linspace(0, 1, num_out_rows)
    out_image = np.empty(
        (out_cols.size, out_rows.size, channels), dtype=image.dtype)
    for channel in range(channels):
        interpolator = interpolate.RectBivariateSpline(
            x=in_cols,
            y=in_rows,
            z=image[:,:,channel])
        out_image[:,:,channel] = interpolator(out_cols, out_rows)
    return out_image

def convert(filename):
    with open(filename) as fh:
        image = read_image(fh)
    scaled_image = scale_image(image)
    brightness = rgb_to_brightness(scaled_image)
    indices = (brightness * CHAR_MAPPING.size / 255).astype(int)
    ascii_image = np.empty(indices.shape, CHAR_MAPPING.dtype)
    for index, value in np.ndenumerate(indices):
        ascii_image[index] = CHAR_MAPPING[value]
    return ascii_image

def process_file(filename):
    ascii_image = convert(filename)
    for line in ascii_image.T:
        print(''.join(np.repeat(line, 1)))

if __name__ == '__main__':
    process_file('ascii-pineapple.txt')
