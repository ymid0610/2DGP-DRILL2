from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
shape = 0
Cx = 400
Cy = 300
r = 210

angle = ((3*math.pi) / 2)

while True:
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if shape == 0:
        if x < 770:
            x += 5
        else:
            x = 770
            shape = 1
    elif shape == 1:
        if y < 555:
            y += 5
        else:
            y = 555
            shape = 2
    elif shape == 2:
        if x > 30:
            x -= 5
        else:
            x = 30
            shape = 3
    elif shape == 3:
        if y > 90:
            y -= 5
        else:
            y = 90
            shape = 4
    elif shape == 4:
        if x < 400:
            x += 5
        else:
            x = 400
            shape = 5
            angle = 4.71239
    elif shape == 5:
        if angle >= ((3*math.pi) / 2) - (2 * math.pi):
            x = Cx + r * math.cos(angle)
            y = Cy + r * math.sin(angle)
            angle -= 0.05
        else:
            shape = 0
            x = 400
            y = 90
    delay(0.002)