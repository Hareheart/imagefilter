# run pip install pillow to install
from PIL import Image
import sys

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    if sys.argv[1] == "flip_image":
        flip_image(image)
    elif sys.argv[1] == "shrink_image":
        shrink_image(image)


def flip_image():
    pass

def shrink_image():
    pass

if __name__ == "__main__":
    main()