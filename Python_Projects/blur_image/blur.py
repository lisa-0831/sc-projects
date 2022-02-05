"""
File: blur.py
Name: PEI-WEN(Lisa) WANG
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: (SimpleImage) the original image
    :return new_img: A new image that was blurred
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            count = 0  # how many neighbors (including itself)
            for i in range(-1, 2):  # Control the change of neighbors' x coordinate
                for j in range(-1, 2):  # Control the change of neighbors' y coordinate
                    if (0 <= x+i < img.width) and (0 <= y+j < img.height):
                        img_p = img.get_pixel(x+i, y+j)
                        sum_red += img_p.red
                        sum_green += img_p.green
                        sum_blue += img_p.blue
                        count += 1
            # Blank
            new_img_p = new_img.get_pixel(x, y)
            new_img_p.red = sum_red / count
            new_img_p.green = sum_green / count
            new_img_p.blue = sum_blue / count
    return new_img


def main():
    """
    This file contains a image processing algorithms: blur
    It can show a blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
