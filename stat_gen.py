import tkinter as tk
import time
import random
from PIL import Image, ImageTk, ImageDraw
import sys


# Tunable parameters
LINECNT = 30
XLIM = 400
YLIM = 400
LINEWIDTH = XLIM / (LINECNT*4)



# Utility functions
def import_image(path):
    image = Image.open(path)
    # image = static_bkgnd.resize((XLIM*2, YLIM*2), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    return image

def generate_static(bounds):
    x0, y0, x1, y1 = bounds
    for x in range(x0, x1):
        for y in range(y0, y1):
            # Randomly choose between black (0) and white (1)
            color = random.choice(["black", "white"])
            canvas.create_line(x, y, x+1, y+1, fill=color)

def gen_static_collection(items):
    for item in items:
        generate_static(item)


# Initialize canvas
root=tk.Tk()
canvas=tk.Canvas(root,width=XLIM,height=YLIM)
canvas.pack()


# cur_y = 0
# items = []
# for i in range(LINECNT):
#    items.append((0, cur_y, XLIM, cur_y+RECTH))
#    cur_y += 2*RECTH

# def redraw():
#    canvas.after(10,redraw)
#    gen_static_collection(items)
#    canvas.update()

#generate_static((0, 0, XLIM, YLIM))
# gen_static_collection(items)

# x, y coord arrays
quadrant_coords = [[0, 0, XLIM/2, YLIM/2, True], 
                   [XLIM/2, 0, XLIM, YLIM/2, False], 
                   [0, YLIM/2, XLIM/2, YLIM, False],
                   [XLIM/2, YLIM/2, XLIM, YLIM, True]]

# generate initial McCollough test image
for coords in quadrant_coords:
    x0, y0, x1, y1, horiz = coords
    if horiz:
        line_pos = y0
        for i in range(LINECNT):
            canvas.create_rectangle(x0, line_pos, x1, line_pos+LINEWIDTH, fill = 'black')
            line_pos += LINEWIDTH*2
    else:
        line_pos = x0
        for i in range(LINECNT):
            canvas.create_rectangle(line_pos, y0, line_pos+LINEWIDTH, y1, fill = 'black')
            line_pos += LINEWIDTH*2




root.mainloop()