# run pip install pillow to install
from PIL import Image
import sys

def main():
    # Open image
    image = Image.open('horse.jpg')

    # Show image
    image.show()

    width, height = image.size
    new_image = Image.new("RGB", (image.size), "white")

    if sys.argv[1] == "flip_image":
        flip_image(image, width, height, new_image)
    elif sys.argv[1] == "shrink_image":
        shrink_image(image)
    elif sys.argv[1] == "hide_image":
        hide_image(image)


def flip_image(image, width, height, new_image):
    t = []
    a = 0
    for x in range(width):
        t.append(image.getpixel(x, 0))
        



def shrink_image(image):
    # get the height and width
    width, height = image.size

    # Divide width and height of new image by 2 and subtract last row and column if width/height is odd numbered
    new_width = int((width / 2) - (width % 2))
    new_height = int((height / 2) - (height % 2))

    # create a new image of half the size as the original
    shrinked_image = Image.new("RGB", (new_width, new_height), "white")

    # coordinate points for where to place pixel in new image
    new_x = 0
    new_y = 0

    for x in range(0, width, 2):
        for y in range(0, height, 2):
            # get the rgb values of four corresponding pixels
            r1, g1, b1 = image.getpixel((x, y))
            r2, g2, b2 = image.getpixel((x + 1, y))
            r3, g3, b3 = image.getpixel((x, y + 1))
            r4, g4, b4 = image.getpixel((x + 1, y + 1))

            # take average rgb values
            avg_r = int((r1 + r2 + r3 + r4) / 4)
            avg_g = int((g1 + g2 + g3 + g4) / 4)
            avg_b = int((b1 + b2 + b3 + b4) / 4)

            # put average rgb into the pixel
            shrinked_image.putpixel((new_x, new_y), (avg_r, avg_g, avg_b))

            # move to next row
            new_y += 1
        # move to next column
        new_x += 1

        # move back to first row
        new_y = 0

    # open the new image
    shrinked_image.show()


def hide_image(image):
    pass


if __name__ == "__main__":
    main()