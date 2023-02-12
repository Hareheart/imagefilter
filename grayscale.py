# run pip install pillow to install
from PIL import Image

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # Initializes formulas and prompts user
    print("Algorithm 1: gray = (r + g + b) / 3 ")
    print("Algorithm 2: gray = (0.2989 * r) + (0.5870 * g) + (0.1140 * b)")
    print()
    alt_formula = input("Use algorithm 1 or 2? Type '1' or '2': ")

    grayscale(image, alt_formula, width, height)


def grayscale(image, alt_formula, width, height):
    # create a new image of the same size as the original
    grayscale_image = Image.new("RGB", (image.size), "white")

    # place a pixel from the original image into the new image
    for x in range(width):
        for y in range(height):
            # get the rgb values of a pixel at a certain coordinate
            r, g, b = image.getpixel((x, y))
            if alt_formula == "1":
                gray = int((r + g + b)/3)
                grayscale_image.putpixel((x, y), (gray, gray, gray))
            elif alt_formula == "2":
                gray = int((0.2989 * r) + (0.5870 * g) + (0.1140 * b))
                grayscale_image.putpixel((x, y), (gray, gray, gray))

    # open the new image
    grayscale_image.show()


if __name__ == "__main__":
    main()