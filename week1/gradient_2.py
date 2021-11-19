def red_gradiant_4(start: number, hue: number):
    global speed, j, sat22
    sat22 = 0
    speed = 200
    j = start
    while j < start + 10:
        light.set_pixel_color(j % 10, get_color(hue, sat22))
        sat22 = sat22 + 25
        pause(speed)
        j += 1
    sat22 = 225
    j = start
    while j < start + 10:
        light.set_pixel_color(j % 10, get_color(hue, sat22))
        sat22 = sat22 - 25
        pause(speed)
        j += 1


def get_color(hue: number, sat: number):
    return light.hsv(hue, sat, 255)
def red_sat(sat2: number):
    return light.hsv(255, sat2, 255)
sat22 = 0
j = 0
speed = 0
light.show_animation(light.rainbow_animation, 500)

def on_forever():
    red_gradiant_4(0, 150)
    pause(5000)
forever(on_forever)
