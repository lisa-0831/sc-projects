"""
File: best_photoshop_award.py
Name: PEI-WEN(Lisa) WANG
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def combine_background(background_img, body_img):
    """
    :param background_img: (SimpleImage) the original image of background
    :param body_img: (SimpleImage) the original image of figure's body
    :return body_img: The updated image with background
    """
    for x in range(body_img.width):
        for y in range(body_img.height):
            body_img_p = body_img.get_pixel(x, y)
            background_img_p = background_img.get_pixel(x, y)

            avg = (body_img_p.red + body_img_p.green + body_img_p.blue) // 3
            if avg >= 220:  # white space (aka the background)
                body_img_p.red = background_img_p.red
                body_img_p.green = background_img_p.green
                body_img_p.blue = background_img_p.blue

    return body_img


def combine_figure(background_img, figure_img):
    """
    :param background_img: (SimpleImage) the original image of background
    :param figure_img: (SimpleImage) the original image of figure
    :return figure_img: The updated image with background
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_img_p = figure_img.get_pixel(x, y)
            background_img_p = background_img.get_pixel(x, y)

            bigger = max(figure_img_p.red, figure_img_p.blue)
            if figure_img_p.green > (bigger*2):  # it's green screen
                figure_img_p.red = background_img_p.red
                figure_img_p.green = background_img_p.green
                figure_img_p.blue = background_img_p.blue

    return figure_img


def main():
    """
    This file contains two image processing algorithms: combine_background and combine_figure
    It can combine the images of the background and the figure.
    """
    body = SimpleImage('image_contest/body.png')
    head = SimpleImage('image_contest/figure.png')
    stage = SimpleImage('image_contest/background.png')
    background = combine_background(stage, body)
    result = combine_figure(background, head)
    result.show()


if __name__ == '__main__':
    main()
