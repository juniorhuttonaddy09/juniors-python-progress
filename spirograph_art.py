"""
Rainbow Spirograph Art
A small Python program that draws glowing rainbow patterns on a black screen.
It only uses Python's built in libraries, so there is nothing to install.

Run it with:  python spirograph_art.py
"""

import colorsys
import turtle

# ---------- SETTINGS (change these to make your own style) ----------
RINGS = 5            # how many layers the pattern has
BASE_RADIUS = 50     # size of the smallest circles
RADIUS_GROWTH = 35   # how much bigger each new layer gets
BASE_CIRCLES = 36    # circles in the first layer
EXTRA_CIRCLES = 12   # extra circles added to every new layer
LINE_WIDTH = 2       # thickness of the lines
TITLE = "Rainbow Spirograph Art"
# --------------------------------------------------------------------


def rainbow(position, offset=0.0):
    """Turn a number between 0 and 1 into a bright rainbow color."""
    hue = (position + offset) % 1.0
    return colorsys.hsv_to_rgb(hue, 1.0, 1.0)


def draw_ring(pen, radius, circles, offset):
    """Draw one layer made of many circles turned a little each time."""
    turn_angle = 360 / circles
    for i in range(circles):
        pen.pencolor(rainbow(i / circles, offset))
        pen.circle(radius)
        pen.right(turn_angle)


def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("black")
    screen.title(TITLE)
    screen.tracer(4, 0)  # draw faster, updating the screen every 4 steps

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(LINE_WIDTH)

    for ring in range(RINGS):
        radius = BASE_RADIUS + ring * RADIUS_GROWTH
        circles = BASE_CIRCLES + ring * EXTRA_CIRCLES
        offset = ring / RINGS  # each layer starts on a different color

        pen.penup()
        pen.home()
        pen.setheading(ring * 7)  # tilt each layer slightly
        pen.pendown()
        draw_ring(pen, radius, circles, offset)

    # A glowing title in the middle when the art is done
    pen.penup()
    pen.home()
    pen.color("white")
    pen.write("Made with Python", align="center", font=("Courier", 16, "bold"))

    screen.update()
    print("Done! Click the window to close it.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
