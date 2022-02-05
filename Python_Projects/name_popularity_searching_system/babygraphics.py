"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

File: babygraphics.py
Name: PEI-WEN(Lisa) WANG
Showing the change of the number of names in each year.
"""

import tkinter
import babynames
import babygraphicsgui as gui

# Constants
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space
    return x_coordinate


def get_y_coordinate(rank):
    """
    Input:
        rank (str): The rank of the name associated
                              with the specified year.
    Returns:
        y_coordinate (int): The y coordinate of the name associated
                              with the specified year.
    """
    space = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 999
    y_coordinate = GRAPH_MARGIN_SIZE + space * (int(rank) - 1)
    return y_coordinate


def get_color(name_index):
    """
    Input:
        name_index (int): The index of the name in the lookup_names list
    Returns:
        color (str): The color of the name associated with the name index.
    """
    color = COLORS[-1]
    remainder = (name_index + 1) % len(COLORS)
    if remainder != 0:
        color = COLORS[remainder - 1]
    return color


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)  # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)  # Bottom line

    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(year), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for name in lookup_names:
        rank_dict = name_data[name]                                         # The dictionary is {'year': 'rank'}
        color = get_color(lookup_names.index(name))
        x_coordinate_lst, y_coordinate_lst = list(), list()                 # For drawing lines

        for year in YEARS:                                                  # Create text
            x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
            x_coordinate_lst.append(x_coordinate)                           # Remember the coordinate of x
            if str(year) not in rank_dict:
                canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=(name, '*'),
                                   anchor=tkinter.SW, fill=color)
                y_coordinate_lst.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)  # Remember the coordinate of y
            else:
                y_coordinate = get_y_coordinate(rank_dict[str(year)])
                canvas.create_text(x_coordinate + TEXT_DX, y_coordinate, text=(name, rank_dict[str(year)]),
                                   anchor=tkinter.SW, fill=color)
                y_coordinate_lst.append(y_coordinate)                       # Remember the coordinate of y

        for i in range(len(YEARS) - 1):                                     # Create line
            canvas.create_line(x_coordinate_lst[i], y_coordinate_lst[i], x_coordinate_lst[i+1], y_coordinate_lst[i+1],
                               width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
