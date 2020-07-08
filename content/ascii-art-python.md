Title: Ascii-Art Conversion Using Python
Date: 2020-07-08T03:57:16+00:00
Category: Computers
Tags: Software, Python
Slug: ascii-art-python

I recently came across an excellent [blog post][1] which has some suggestions
on interesting short-term coding projects. I think these projects are a fun way
to learn a new language (lately, I've been interested in learning Nim and
Ocaml, for reasons that I'll try to explain some other time).

For a start, I decided to try doing an implementation in Python. The full code can be found [here][2]. Here was my methodology:

# Loading the Image

I decided that I didn't want to mess around with third party libraries to load
the image into the program, so I used ImageMagick to convert the [suggested
image][3] to a text file like so:

    :::bash
    convert ascii-pineapple.jpg ascii-pineapple.txt

The result was a text file which looks like this:

    :::text
    # ImageMagick pixel enumeration: 700,467,65535,srgb
    0,0: (1,116,209)  #0174D1  srgb(1,116,209)
    1,0: (1,116,209)  #0174D1  srgb(1,116,209)
    2,0: (1,116,209)  #0174D1  srgb(1,116,209)
    3,0: (1,116,209)  #0174D1  srgb(1,116,209)

So parsing it was a fairly straightforward task. The first line contains
important metadata (the width and height of the file) which I use to initialise
a numpy array. The code assumes that there are always 3 channels (rgb) and
parses each line into the appropriate index of the loaded image array.

    :::python
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

# Scaling the Image

Immediately, there's a problem: ascii characters are much wider than a single
pixel/dot from the image, so it's a good idea to scale the image to an
appropriate size. I chose about 630 columns since that was the maximum that my terminal would display after zooming out as much as possible (but in theory, one could always determine it [programmatically][4] as well).

I wanted to use my own method to scale the image, and I wanted to use bicubic
interpolation to get a reasonable quality result. `scipy` provides a few ways
to perform interpolation; since the image is a rectilinear grid, I was able to
use [RectBivariateSpline][5] for interpolation. Determining exactly how to
scale the image was the hardest part of this project, in particular because (as
the blog post mentions), it's a good idea to scale the image 3 times larger in
width (due to the aspect ratio of terminal characters), and this was a good
place to do it. Finally, I wanted to scale the image before the RGB channels
were converted to brightness, which I'm guessing had a slight improvement on
the resolution of the final image.

Ultimately, I found that the easiest thing to do was define a coordinate system
such that the input image's opposite corners are `((0, 0), (1, 1))`. The input
grid points then become a simple `linspace` from 0 to 1 with the number of
points being equal to the number of input rows/columns. The total number of
output columns was also a linspace from 0 to 1 with `MAX_WIDTH` columns, and a
proportional number of rows to preserve the aspect ratio. Finally, to achieve
the 3x scaling in width, the total number of rows selected was reduced by a
factor of 3.

Here is the result:

    :::python
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

# Remaining Conversion Steps

After that, all that was left was to

1. convert each pixel (still with 3 channels for RGB) to brightness using the
   luminosity formula provided in the blog post (`.21 R + .72 G + .07 B`)

2. generate a lookup table mapping brightnesses to ascii characters

3. map the brightness images to ascii characters using the lookup table

4. print the image

The third step was actually the most annoying, because I couldn't figure out a vectorised way to achieve it. The last step was also annoying because iteration over the image went by columns rather than rows, so I had to take the transpose.

    :::python
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

# Final Result

Once again, here's [the code][2] and [here's][6] the final result of the pineapple photo provided by the blog. Make sure to zoom out (ctrl - on XUL-based browsers) if the lines wrap.

# Retrospective

Ultimately, it was a fun project that was made quite easy, in particular by
using `numpy` for arrays, `scipy` for interpolation, and ImageMagick to
shortcut loading the image using an image processing library. While I don't
regret using `numpy` because Python doesn't have any native array support, I
would be most eager to drop the `scipy` dependency and write my own bicubic
interpolator. I think I would enjoy the challenge of reading the math and
converting it to code.

I also hope to use this example to reimplement this project using Nim and Ocaml, which are two languages I find quite exciting because of their feature sets. Hopefully I will be able to do one of them soon.

[1]: https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
[2]: {static}/code/ascii-art.py
[3]: https://robertheaton.com/images/ascii-pineapple.jpg
[4]: https://unix.stackexchange.com/a/197171
[5]: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.RectBivariateSpline.html#scipy.interpolate.RectBivariateSpline
[6]: {static}/code/pineapple.txt
