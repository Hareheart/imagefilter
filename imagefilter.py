# run pip install pillow to install
from PIL import Image

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # place a pixel from the original image into the new image
    for x in range(width):
        for y in range(height):
            # get the rgb values of a pixel at a certain coordinate
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (r, g, b))

    # open the new image
    new_image.show()


if __name__ == "__main__":
    main()