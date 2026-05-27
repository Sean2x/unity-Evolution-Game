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

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# ---------------------------------
# Custom basis vectors
# ---------------------------------

# 1 X unit = 5 right, 4 up
X_AXIS = (5, 4)

# 1 Y unit = 9 right, 2 down
Y_AXIS = (9, -2)

# 1 Z unit = 5 up
Z_AXIS = (0, 5)

POINT_RADIUS = 2

# ---------------------------------
# 3D -> Screen projection
# ---------------------------------

def ProjectPoint(x, y, z):

    sx = (
        x * X_AXIS[0] +
        y * Y_AXIS[0] +
        z * Z_AXIS[0]
    )

    sy = (
        x * X_AXIS[1] +
        y * Y_AXIS[1] +
        z * Z_AXIS[1]
    )

    return (
        CENTER_X + sx,
        CENTER_Y - sy
    )

# ---------------------------------
# Draw point
# ---------------------------------

def DrawPoint(x, y, z, color="lime"):

    sx, sy = ProjectPoint(x, y, z)

    r = POINT_RADIUS

    canvas.create_oval(
        sx-r, sy-r,
        sx+r, sy+r,
        fill=color,
        outline=color
    )

# ---------------------------------
# Draw line
# ---------------------------------

def DrawLine(p1, p2, color="cyan"):

    x1, y1 = ProjectPoint(*p1)
    x2, y2 = ProjectPoint(*p2)

    canvas.create_line(
        x1, y1,
        x2, y2,
        fill=color
    )

# ---------------------------------
# Draw axes
# ---------------------------------

def DrawAxes(length=30):

    # X axis
    DrawLine((-length,0,0), (length,0,0), "red")

    # Y axis
    DrawLine((0,-length,0), (0,length,0), "green")

    # Z axis
    DrawLine((0,0,-length), (0,0,length), "blue")

# ---------------------------------
# Laser grid
# ---------------------------------

def DrawGrid(size=20, z=0):

    for x in range(-size, size + 1):

        DrawLine(
            (x, -size, z),
            (x, size, z),
            "#00ff88"
        )

    for y in range(-size, size + 1):

        DrawLine(
            (-size, y, z),
            (size, y, z),
            "#00ff88"
        )

# ---------------------------------
# Random glowing points
# ---------------------------------

def SpawnRandomPoints(count=100):

    for _ in range(count):

        x = random.randint(-20, 20)
        y = random.randint(-20, 20)
        z = random.randint(-10, 10)

        DrawPoint(x, y, z, "white")

# ---------------------------------
# Main
# ---------------------------------

DrawGrid(25, 0)

DrawAxes(30)

SpawnRandomPoints(150)

window.mainloop()