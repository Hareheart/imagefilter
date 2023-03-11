# run pip install pillow to install
from PIL import Image
import sys

# PASS IN COMMAND LINE ARGUMENT TO RUN MODULES
# "rgb_scale", "grayscale", "flip_image", "shrink_image", and "hide_image" are the options

def main():
    # Open image
    image = Image.open('horse.jpg')

    # Show image
    image.show()

    if sys.argv[1] == "grayscale":
        # Initializes formulas and prompts user
        print("Algorithm 1: gray = (r + g + b) / 3 ")
        print("Algorithm 2: gray = (0.2989 * r) + (0.5870 * g) + (0.1140 * b)")
        print()
        alt_formula = input("Use algorithm 1 or 2? Type '1' or '2': ")

        grayscale(image, alt_formula)

    elif sys.argv[1] == "rgb_scale":
        rgb_scale(image)
    elif sys.argv[1] == "flip_image":
        flip_image(image)
    elif sys.argv[1] == "shrink_image":
        shrink_image(image)
    elif sys.argv[1] == "hide_image":
        hide_image(image)


def rgb_scale(image):
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


def grayscale(image, alt_formula):
    # get the height and width
    width, height = image.size

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


def flip_image(image):
    # Created by Matthew

    # get the height and width
    if sys.argv[2] == "horizontal":
        horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal.show()
    if sys.argv[2] == "vertical":
        vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
        vertical.show()


def shrink_image(image):
    # Created by David

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
    # Created by Matthew and David

    # get the height and width
    width, height = image.size

    # create a new image of the same size as the original
    hidden_image = Image.new("RGB", (image.size), "white")

    # ask user whether they want message or image
    hide_type = input("Hide message or image? ")
    if hide_type == "message":
        # asks user for message to be hidden in image
        message = input("Enter your desired message: ")

        # divides message into array
        divided_message = []
        for char in message:
            divided_message.append(char)

        for x in range(width):
            for y in range(height):
                for letter in divided_message:
                    # get the rgb values of a pixel at a certain coordinate
                    r, g, b = image.getpixel((x, y))

                    # take first three binary values of r and g values, and take first two of b value
                    # 8 pixels total will be used for modification
                    r = (bin(r)[2:5])
                    g = (bin(g)[2:5])
                    b = (bin(b)[2:4])

                    # turn message into integer values corresponding to ASCII chart
                    ints = ord(letter)

                    # turn ints to binary
                    binary = bin(ints)

                    # split binary message into three parts and add each to corresponding rgb value
                    r_bin_val = ((binary)[2:5])
                    g_bin_val = ((binary)[5:8])
                    b_bin_val = ((binary)[8:10])

                    # creates new rgb values with message values
                    new_r = int(r + r_bin_val)
                    new_g = int(g + g_bin_val)
                    new_b = int(b + b_bin_val)

                    # adds new pixels to hidden image
                    hidden_image.putpixel((x, y), (new_r, new_g, new_b))

                    # if there are no characters left in the message, image won't be further altered from original
                    if letter == divided_message[-1]:
                        for x in range(width):
                            for y in range(height):
                                r, g, b = image.getpixel((x, y))
                                hidden_image.putpixel((x, y), (r, g, b))
        
                        # open the new image
                        hidden_image.show()
                        sys.exit()

    if hide_type == "image":
        # ask user for which image to pick from list
        choices = ["buster.png", "hyena.jpg", "jump.jpeg", "kitty.png", "latestart.jpg", "nightbee.png", "owlbear.jpg", "philip.jpg", 
                   "thanksgiving.jpg"]
        print(choices)
        image_choice = input("Choose an image: ")
        
        second_hidden_image = Image.open(image_choice)
        second_width, second_height = second_hidden_image.size

        new_x = 0
        new_y = 0

        for x in range(width):
            for y in range(height):
                for new_x in range(second_width):
                    for new_y in range(second_height):
                        # get the rgb values of a pixel at a certain coordinate at first image
                        r1, g1, b1 = image.getpixel((x, y))

                        # take first four binary values of rgb values from first image
                        r1 = (bin(r1)[2:6])
                        g1 = (bin(g1)[2:6])
                        b1 = (bin(b1)[2:6])

                        # get the rgb values of a pixel at a certain coordinate at second image
                        r2, g2, b2 = second_hidden_image.getpixel((new_x, new_y))
                            
                        # take first four binary values of rgb values from second image
                        r2 = (bin(r2)[2:6])
                        g2 = (bin(g2)[2:6])
                        b2 = (bin(b2)[2:6])

                        # creates new rgb values with first four pixels of first image + first four pixels of second image
                        new_r2 = int(r1 + r2)
                        new_g2 = int(g1 + g2)
                        new_b2 = int(b1 + b2)

                        # adds first four pixels of second image to first image
                        hidden_image.putpixel((x, y), (new_r2, new_g2, new_b2))

                        # if second image reaches last width or height pixel, image won't be further altered from original
                        if str(new_x) == (str(second_width)[-1]) and str(new_y) == (str(second_height)[-1]):
                            for x in range(width):
                                for y in range(height):
                                    r, g, b, = image.getpixel((x, y))
                                    hidden_image.putpixel((x, y), (r, g, b))

                            # open the new image
                            hidden_image.show()
                            sys.exit()


if __name__ == "__main__":
    main()