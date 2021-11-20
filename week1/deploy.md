# Deploying programs onto the device

There are two methods for deploying a program onto the Circuit Playground (CP). 
The first is simple, but doesn't always work; the second is foolproof, but 
a little more complicated to explain. 

## Method 1: WebUSB (ie, via the website)

* Connect the CP to the computer. 
* In the MakeCode editor, click the three dots next to the "Download" button 
    and select "Connect Device"
    (OR: Click the "Settings" button/gear icon in the upper left hand corner of 
     the screen, and click "Connect Device")
* Depending on your computer (PC/Mac) and browser (Chrome vs something else), and 
   your security settings, 
   what happens next might vary. Basically, select "Connect" in all the places 
   that it comes up. It *should* show success. 
* Click the "Download" button, and at that point, the program running on the emulator 
   (in the browser) gets copied to the device, and should start running. 


## Method 2: Drag and Drop/Copy files (ie, using the File Explorer/Finder)

* Connect the CP to the computer. 
* It shows up in the Finder (Mac) or File Explorer (PC) as a new mounted drive. 
   * It should be named ```CPLAYBOOT```. 
* In the Makecode Editor, click "Download". 
   * If it looks like it's not downloading a file, you might try click the three-dot 
      button and selecting "Download as file". 
   * The program is downloaded as a file and stored on your computer
   * It should be named something like ```maker-adafruit-[stuff].uf2```
* Go to the Finder/File Explorer. 
* Drag and drop the downloaded file from the ```Downloads``` directory into the 
   ```CPLAYBOOT``` directory. 


## All Methods: 

* When you plug the CP in to the computer, the lights on the CP all turn red; when the 
   CP is ready to be copied to, all the lights turn green. 
* If it seems like something isn't happening as you expect, try pressing the 
   "reset" button on the CP: It's a tiny little button right in the middle of the board, 
   between two larger buttons. 
   * That basically resets the device and usually helps address any issues. 


## More Help/Troubleshooting

If something still isn't working right, let me know and I'll try to debug, either over 
Zoom, or the phone, or anything else. 

