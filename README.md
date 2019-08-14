# Hero's Spell List

For a video explanation, [click here](https://www.youtube.com/watch?v=HBB9Zq3s9gQ). It will make more sense what this code is trying to accomplish if you've watched this video first.

## HeroOCR.py

Reads the spell list from Hero's Down Special in Super Smash Bros. Ultimate.

HeroOCR.py is the main script. Requires OpenCV and PyTesseract to work properly. [Here is the video](https://youtu.be/_5ml_Y9hqG8) I borrowed some code from and learned how to set up Tesseract.

If you want to use this yourself, you must have a window open with video feed from your Switch. Then you must edit the screen coordinates in the funciton "grab_screens_2" on line 90. Ensure that this is a bounding box of dimensions 300px by 200px, and that the spell list fits comfortably within those dimensions. You can find those coordinates easily with [this utility.](https://www.adminsehow.com/2012/03/realtime-mouse-position-monitor-tool/)

This process is most easily accomplished by opening [OBS](https://obsproject.com/) and increasing the size of your capture source in the preview until the spell list takes up a 300px by 200px portion of your desktop.

Edit the final line to choose how many spell lists you wish to capture, then build the script. The capture window must remain visible on-screen at all times. Once all images are screengrabbed and analyzed, the spell lists will be output to OCR_List.csv in the current directory.

## HeroSim.py

Simulates the same algorithm which Super Smash Bros Ultimate seems to use to generate spell lists. Edit the final line to choose how many spell lists to simulate. Outputs to Simulate.csv in the current directory.

## Special Thanks

[bertrandom](https://github.com/bertrandom/snowball-thrower) for your Snowball Thrower, [shinyquagsire23](https://github.com/shinyquagsire23/Switch-Fightstick) for your Splatoon Post Printer, and [progmem](https://github.com/progmem/Switch-Fightstick) for laying the controller groundwork, made the automation side of this project far easier than is really fair.

[Luke Garbutt](https://youtu.be/_5ml_Y9hqG8) on Youtube, this was the workaround I used when OpenCV couldn't detect my Elgato Capture Card. Everything else fell into place naturally around what I borrowed from this video. Thanks.
