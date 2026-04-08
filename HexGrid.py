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

P = 9
Q = 7
HexRad = 20
PointRad = 5

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

MakeGrid(P, Q)
for i in range(0, 8):
    point = RandomPointOnGrid(P, Q)
    MakePointBlue(*PointOnGrid(*point))
    MakePointsBlue(PointsOnGrid(SurroundingPoints(*point)))






window.mainloop()