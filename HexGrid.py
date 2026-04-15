import tkinter as tk
import random
from numpy import sqrt

current_width = 700
current_height = 600

window = tk.Tk()
window.title("Dot window")
window.geometry(f"{current_width}x{current_height}")

canvas=tk.Canvas(window, width=current_width, height=current_height, bg="#121212")
canvas.pack(fill="both", expand="true")

P = 27
Q = 21
HexRad = 5
PointRad = 2

def MakePoint(x_offset, y_offset):    
    x, y, r = (current_width // 2) + x_offset, (current_height // 2) - y_offset, PointRad
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="Green")

def MakePointBlue(x_offset, y_offset):    
    x, y, r = (current_width // 2) + x_offset, (current_height // 2) - y_offset, PointRad
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

def MakePointsBlue(points):
    for x_offset, y_offset in points:
        x = (current_width // 2) + x_offset
        y = (current_height // 2) - y_offset
        r = PointRad
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

def PointOnGrid(x, y):
     if x % 2 == 1:
        return (HexRad * sqrt(3) * x, 2 * HexRad * y )
     else:
        return (HexRad * sqrt(3) * x, 2 * HexRad * y - HexRad)
     
def PointsOnGrid(coords):
    result = []
    for x, y in coords:
        if x % 2 == 1:
            result.append((HexRad * sqrt(3) * x, 2 * HexRad * y))
        else:
            result.append((HexRad * sqrt(3) * x, 2 * HexRad * y - HexRad))
    return result

def MakeGrid(x, y):
 for i in range(-x, x+1):
    for j in range(-y-1, y):
        if i % 2 == 1:
            MakePoint(HexRad * sqrt(3) * i, (2 * HexRad * j))
        else:
            MakePoint(HexRad * sqrt(3) * i, 2 * HexRad * j + HexRad)

def SurroundingPoints(x, y):
    # MakePointBlue(*PointOnGrid(x, y))
    if x % 2 == 1:
        # MakePointBlue(*PointOnGrid(x+1, y))
        # MakePointBlue(*PointOnGrid(x-1, y))
        # MakePointBlue(*PointOnGrid(x, y+1))
        # MakePointBlue(*PointOnGrid(x, y-1))
        # MakePointBlue(*PointOnGrid(x+1, y+1))
        # MakePointBlue(*PointOnGrid(x-1, y+1))
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y+1))
    else:
        # MakePointBlue(*PointOnGrid(x+1, y))
        # MakePointBlue(*PointOnGrid(x-1, y))
        # MakePointBlue(*PointOnGrid(x, y+1))
        # MakePointBlue(*PointOnGrid(x, y-1))
        # MakePointBlue(*PointOnGrid(x+1, y-1))
        # MakePointBlue(*PointOnGrid(x-1, y-1))
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y-1), (x-1, y-1))

def RandomPointOnGrid(x, y):
    return (random.randint(-x+1, x), random.randint(-y, y-1))

# MakeGrid(P, Q)
# for i in range(0, 8):
#     point = RandomPointOnGrid(P, Q-1)
#     MakePointBlue(*PointOnGrid(*point))
#     MakePointsBlue(PointsOnGrid(SurroundingPoints(*point)))

# ----------------------------
# Step 1: build green grid slowly
# ----------------------------
green_points = []

def build_grid(i=-P, j=-Q-1):
    if i > P:
        start_blue_phase()
        return

    if j > Q:
        window.after(1, build_grid, i + 1, -Q - 1)
        return

    green_points.append((i, j))
    MakePoint(*PointOnGrid(i, j))

    window.after(1, build_grid, i, j + 1)


# ----------------------------
# Step 2: spawn blue points with delay
# ----------------------------
blue_targets = []

def start_blue_phase():
    global blue_targets
    blue_targets = [RandomPointOnGrid(P, Q - 1) for _ in range(8)]
    spawn_blue(0)

def spawn_blue(index):
    if index >= len(blue_targets):
        return

    point = blue_targets[index]

    MakePointBlue(*PointOnGrid(*point))

    for n in SurroundingPoints(*point):
        MakePointBlue(*PointOnGrid(*n))

    window.after(300, spawn_blue, index + 1)


# ----------------------------
# Start animation
# ----------------------------
build_grid()





window.mainloop()

