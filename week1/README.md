# Week 1: Gradient Neopixels

This week we're going to start by making our Circuit Playgrounds display a smooth 
gradient of color. 


## Step 1: Getting the Circuit Playground going

[MakeCode](https://maker.makecode.com/#editor)

* Create a new project, based on the Circuit Playground
* Use the block editor to build a simple program with the lights
* Plug your Circuit Playground into the computer
* Click the "Reset" button (super tiny, in the middle of the board). 
    * The board lights should turn red, and then turn green. 
* Next to the big blue "Download" button, click the little button with three dots. 
    * Click "Connect to Device"
* Follow the dialogs. 

At this point, your new program should be on the device, and the lights should be 
doing what you told them to! 

## Step 2: Plan your approach.

The first step in any project it to think, make sure you understand the problem 
that you are trying to solve, and to identify a plan to attack it. The process of 
understanding the problem and choosing a plan usually is iterative: we ask some questions, 
maybe write some code to get an answer or test an idea, and then either go back 
to the drawing board or move on to the next step. 

So let's think: What's this program really doing? 



## Potentially Relevant Information

To set the color of a neopixel: 

```
light.set_pixel_color(6, 0xFF0000)
```

(this sets the neopixel at position 6 to the color red)

To convert numbers to a light color: 

```
light.rgb(255, 0, 0)

```
(this returns the color red)


To set the color of a neopixel to red using HSV: 
```
light.set_pixel_color(6, light.hsv(255, 255, 255))
```




# Resources

[Color Picker](https://colorpicker.me/#f87eab)




# Takeaways


# Challenges


