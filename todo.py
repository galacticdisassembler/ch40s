#!/usr/bin/env python

import argparse

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky.auto import auto

print("TODO tasklist on your inky phat display!")

try:
    inky_display = auto(ask_user=True, verbose=True)
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

parser = argparse.ArgumentParser()
parser.add_argument("--task1", "-1", type=str,
                    required=True, help="Your first task")
parser.add_argument("--task2", "-2", type=str,
                    required=False, help="Your second task")
parser.add_argument("--task3", "-3", type=str,
                    required=False, help="Your third task")
parser.add_argument("--task4", "-4", type=str,
                    required=False, help="Your fourth task")
parser.add_argument("--task5", "-5", type=str,
                    required=False, help="Your fifth task")
args, _ = parser.parse_known_args()

# inky_display.set_rotation(180)
try:
    inky_display.set_border(inky_display.RED)
except NotImplementedError:
    pass

# Flipping display because I need it
inky_display.h_flip = True
inky_display.v_flip = True

offset_y = 4
padding_x = 8
padding_y = 18


def offset_calc(padding_y):
    global offset_y
    offset_y += padding_y
    return offset_y


# Create a new canvas to draw on

img = Image.new("P", inky_display.resolution)
draw = ImageDraw.Draw(img)

# Load the fonts

font1 = ImageFont.truetype("/home/pi/fonts/VT323.ttf", 22)
font2 = ImageFont.truetype("/home/pi/fonts/Monterey.ttf", 18)
font3 = ImageFont.truetype("/home/pi/fonts/lcd7.ttf", 11)
font4 = ImageFont.truetype("/home/pi/fonts/Prototype.ttf", 18)
font5 = ImageFont.truetype("/home/pi/fonts/gang_wolfik.ttf", 32)
fontemj = ImageFont.truetype("/home/pi/fonts/NotoSansSC-Regular.otf", 12)
# Grab the task1 to be displayed

task1 = args.task1

# Top and bottom y-coordinates for the white strip

y_top = int(inky_display.height * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.height * (4.0 / 10.0))

# Draw the red, white, and red strips

todo_w, todo_h = fontemj.getsize("TODO:        (╯°□°）╯︵ ┻━┻".upper())
todo_x = 1
todo_y = offset_y
for y in range(0, offset_y + 10):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.WHITE)
draw.text(
    (todo_x, todo_y - 4), "ToDo:         (╯°□°）╯︵ ┻━┻", inky_display.RED, font=fontemj
)

task1_w, task1_h = font1.getsize(task1.upper())
task1_x = padding_x
task1_y = offset_calc(padding_y)
for y in range(14, offset_y + 11):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.RED)
draw.text((task1_x, task1_y - 8),
          str(f"1) {task1}"), inky_display.WHITE, font=font1)


if args.task2 != None:
    task2_w, task2_h = font2.getsize(args.task2.upper())
    task2_x = padding_x
    task2_y = offset_calc(padding_y)

    for y in range(34, offset_y + 11):
        for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.BLACK)
    draw.text(
        (task2_x, task2_y - 6), str(f"2) {args.task2}"), inky_display.WHITE, font=font2
    )


if args.task3 != None:
    task3_w, task3_h = font3.getsize(args.task3.upper())
    task3_x = padding_x
    task3_y = offset_calc(padding_y)

    for y in range(52, offset_y + 11):
        for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.RED)
    draw.text(
        (task3_x, task3_y), str(f"3) {args.task3}"), inky_display.WHITE, font=font3
    )


if args.task4 != None:
    task4_w, task4_h = font4.getsize(args.task4.upper())
    task4_x = padding_x
    task4_y = offset_calc(padding_y)

    for y in range(70, offset_y + 11):
        for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.BLACK)
    draw.text(
        (task4_x, task4_y - 6), str(f"4) {args.task4}"), inky_display.WHITE, font=font4
    )


if args.task5 != None:
    task5_w, task5_h = font5.getsize(args.task5.upper())
    task5_x = padding_x
    task5_y = offset_calc(padding_y)

    for y in range(88, offset_y + 10):
        for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.RED)
    draw.text(
        (task5_x, task5_y - 4), str(f"5) {args.task5}"), inky_display.WHITE, font=font5
    )


inky_display.set_image(img)
inky_display.show()