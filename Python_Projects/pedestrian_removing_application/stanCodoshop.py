"""
File: stanCodoshop.py
Name: PEI-WEN(Lisa) WANG
----------------------------------------------

Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

Users can get a photo without passersby by running this program.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2) ** (1/2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    return [total_red//len(pixels), total_green//len(pixels), total_blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    min_distance = 100000000000
    min_pixel = pixels[0]
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist < min_distance:  # update the pixel with the smallest distance
            min_distance = dist
            min_pixel = pixel
    return min_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for x in range(result.width):
        for y in range(result.height):
            pixels = []
            for i in range(len(images)):  # get pixels that are in different pictures but have the same coordinates
                pixel = images[i].get_pixel(x, y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)

            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red  # update the pixel of result
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
