def on_forever():
    light.onboard_strip().set_gradient(0xffffff, 0x0000ff)
    pause(500)
    light.onboard_strip().set_gradient(0x0000ff, 0xffffff)
    pause(500)

def on_button_a_click():
    pass
input.button_a.on_event(ButtonEvent.CLICK, on_button_a_click)

def red_gradiant():
    global spped
    spped = 200
    light.set_pixel_color(0, red_sat(0))
    pause(spped)
    light.set_pixel_color(1, red_sat(25))
    pause(spped)
    light.set_pixel_color(2, red_sat(50))
    pause(spped)
    light.set_pixel_color(3, red_sat(75))
    pause(spped)
    light.set_pixel_color(4, red_sat(100))
    pause(spped)
    light.set_pixel_color(5, red_sat(125))
    pause(spped)
    light.set_pixel_color(6, red_sat(150))
    pause(spped)
    light.set_pixel_color(7, red_sat(175))
    pause(spped)
    light.set_pixel_color(8, red_sat(200))
    pause(spped)
    light.set_pixel_color(9, red_sat(225))
    pause(spped)
    light.set_pixel_color(10, red_sat(255))
    pause(spped)
    light.set_all(0xffffff)
def on_forever2():
    global spped
    spped = 200
    light.set_pixel_color(0, light.hsv(255, 255, 255))
    light.set_pixel_color(0, red_sat(0))
    pause(spped)
    light.set_pixel_color(1, 0xFFDDDD)
    pause(spped)
    light.set_pixel_color(2, 0xFFCCCC)
    pause(spped)
    light.set_pixel_color(3, 0xFFAAAA)
    pause(spped)
    light.set_pixel_color(4, 0xFF8585)
    pause(spped)
    light.set_pixel_color(5, 0xFF6060)
    pause(spped)
    light.set_pixel_color(6, 0xFF3535)
    pause(spped)
    light.set_pixel_color(7, 0xFF1010)
    pause(spped)
    light.set_pixel_color(8, 0xFF0505)
    pause(spped)
    light.set_pixel_color(9, 0xFF0202)
    pause(spped)
    light.set_pixel_color(10, 0xff0000)
    pause(spped)
    light.set_all(0xffffff)
def red_gradiant_2():
    global spped, sat2
    spped = 200
    sat2 = 0
    for i in range(10):
        light.set_pixel_color(i, red_sat(sat2))
        sat2 = sat2 + 25
        pause(spped)
# light.set_all(0xffffff)
def red_sat(sat: number):
    return light.hsv(255, sat, 255)
def on_forever3():
    global spped, sat22, k
    spped = 200
    sat22 = 0
    k = 9
    while k > -1:
        print(k)
        light.set_pixel_color(k, red_sat(sat22))
        sat22 = sat22 + 25
        pause(spped)
        k += -1
    # light.set_all(0xffffff)
    pause(200)
def red_gradiant_3(start: number):
    global spped, sat2
    spped = 200
    sat2 = 0
    j = start
    while j < start + 10:
        # console.log(j%10)
        light.set_pixel_color(j % 10, red_sat(sat2))
        # console.log(sat2)
        sat2 = sat2 + 25
        pause(spped)
        j += 1
    sat2 = 225
    j = start
    while j < start + 10:
        light.set_pixel_color(j % 10, red_sat(sat2))
        sat2 = sat2 - 25
        # console.log(sat2)
        pause(spped)
        j += 1
    # console.log("done")

k = 0
sat22 = 0
spped = 0
sat2 = 0
# red_gradiant_2()
# on_forever3()
 

def on_forever4():
    red_gradiant_3(0)
    # red_gradiant_3(1)
    # red_gradiant_3(2)
    # red_gradiant_3(3)
    # red_gradiant_3(4)
    # red_gradiant_3(5)
    # red_gradiant_3(6)
    # red_gradiant_3(7)
    # red_gradiant_3(8)
    # red_gradiant_3(9)
    pause(1000)
forever(on_forever4)
