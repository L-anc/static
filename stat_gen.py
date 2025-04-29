import tkinter as tk
import time
import random
from PIL import Image, ImageTk

LINECNT = 10
XLIM = 1500
YLIM = 1000
RECTH = int(YLIM/(LINECNT*2))

root=tk.Tk()
canvas=tk.Canvas(root,width=XLIM,height=YLIM)
canvas.pack()

static_bkgnd = Image.open("static_bkgnd.png")
static_bkgnd = static_bkgnd.resize((XLIM*2, YLIM*2), Image.LANCZOS)
static_bkgnd = ImageTk.PhotoImage(static_bkgnd)


# image_path = "your_image.jpg" 
# image = Image.open(image_path)
# photo_image = ImageTk.PhotoImage(image)

# background_label = tk.Label(window, image=photo_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# background_label.image = photo_image


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


cur_y = 0
items = []
for i in range(LINECNT):
   items.append((0, cur_y, XLIM, cur_y+RECTH))
   cur_y += 2*RECTH



def redraw():
   canvas.after(10,redraw)
   gen_static_collection(items)
   canvas.update()

#generate_static((0, 0, XLIM, YLIM))
# gen_static_collection(items)
canvas.create_image(0, 0, image = static_bkgnd)
root.mainloop()