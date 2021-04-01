# run: python3 -m pip install hsluv
from hsluv import *

def get_input(string):
    pick = input(string)
    return hex_to_hsluv(pick)

def pick_color(name):
    color = get_input(f"{name} hex code: ")
    show_color(color)
    return color

def show_color(color):
    h   = hsluv_to_hex(color)
    rgb = [int(255 * x) for x in hsluv_to_rgb(color)]
    text = [255, 255, 255] if color[2] < 50 else [0, 0, 0]
    print(f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m\033[38;2;{text[0]};{text[1]};{text[2]}m {h} \033[0m")

start = pick_color("start") # hue (0-360), saturation (0-100), lightness (0-100)
end   = pick_color("end")
stops = int(input("enter number of stops: "))
gradient = []

print("gradient:")

for step in range(stops):
    # how far along the curve
    k = step / (stops - 1)
    mix = [
        k * start[0] + (1 - k) * end[0],
        k * start[1] + (1 - k) * end[1],
        k * start[2] + (1 - k) * end[2],
    ]
    gradient.append(mix)

for color in gradient:
    show_color(color)
