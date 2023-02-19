# run pip install pillow to install
from PIL import Image
import sys

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    width, height = image.size
    new_image = Image.new("RGB", (image.size), "white")

    if sys.argv[1] == "flip_image":
        flip_image(image, width, height, new_image)
    elif sys.argv[1] == "shrink_image":
        shrink_image(image)


def flip_image(image, width, height, new_image):
    t = []
    a = 0
    for x in range(width):
        t.append(image.getpixel(x, 0))
        


def shrink_image():
    pass

if __name__ == "__main__":
    main()