"""
File: babygraphics.py
Name: Dorinda
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 年份與年份間的距離
    spacing = (width - 2 * GRAPH_MARGIN_SIZE)/len(YEARS)
    # 年份的x值
    x_coordinate = GRAPH_MARGIN_SIZE + (spacing * year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    l_spacing = GRAPH_MARGIN_SIZE
    canvas.create_line(l_spacing, l_spacing, CANVAS_WIDTH-l_spacing, l_spacing, width=LINE_WIDTH)
    canvas.create_line(l_spacing, CANVAS_HEIGHT-l_spacing, CANVAS_WIDTH-l_spacing,
                       CANVAS_HEIGHT-l_spacing, width=LINE_WIDTH)

    # 加入年份文字與直線
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-l_spacing,
                           text=YEARS[i], anchor=tkinter.NW)


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

    # ----- Write your code below this line ----- #

    y_spacing = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2) / MAX_RANK
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        x2, y2 = 0, 0
        rank2 = ""
        if name in name_data:
            for j in range(len(YEARS)-1):
                x1 = get_x_coordinate(CANVAS_WIDTH, j)
                x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
                if str(YEARS[j]) not in name_data[name]:
                    rank1 = "*"
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    rank1 = name_data[name][str(YEARS[j])]
                    y1 = y_spacing * int(rank1) + GRAPH_MARGIN_SIZE
                if str(YEARS[j+1]) not in name_data[name]:
                    rank2 = "*"
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    rank2 = name_data[name][str(YEARS[j+1])]
                    y2 = y_spacing * int(rank2) + GRAPH_MARGIN_SIZE

                canvas.create_line(x1, y1, x2, y2, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(x1+TEXT_DX, y1, text=name+" "+rank1, anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            canvas.create_text(x2+TEXT_DX, y2, text=name+" "+rank2, anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])


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
