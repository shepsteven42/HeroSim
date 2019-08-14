## Hero_Menuer

Automatically presses Down+B repeatedly in Super Smash Bros Ultimate.

#### How to use

Enter training mode on the training stage with your desired character, then disconnect all controllers from your Switch. Plug in the microcontroller either through one of the USB ports on the front of the Switch dock, or through a USB-C to USB-A adapter into the bottom of the Switch. The controller will automatically pair to the console, select the character, and start repeating the Down+B macro.

In case you see issues with controller conflicts while in docked mode, try using a USB-C to USB-A adapter in handheld mode. In dock mode, changes in the HDMI connection will briefly make the Switch not respond to incoming USB commands, skipping parts of the sequence. These changes may include turning off the TV, or switching the HDMI input. (Switching to the internal tuner will be OK, if this doesn't trigger a change in the HDMI input.)

If you would like to use this to write your own script, edit the Joystick.c file's variable named "static const command step". The script will loop through the entire set of commands in this variable ad infinitum.

This repository has been tested using a Teensy 2.0++

#### Compiling and Flashing onto the Teensy 2.0++ or Teensy 2.0
Go to the Teensy website and download/install the [Teensy Loader application](https://www.pjrc.com/teensy/loader.html).  For Linux, follow their instructions for installing the [GCC Compiler and Tools](https://www.pjrc.com/teensy/gcc.html). For Windows, you will need the [latest AVR toolchain](http://www.atmel.com/tools/atmelavrtoolchainforwindows.aspx) from the Atmel site. See [this issue](https://github.com/LightningStalker/Splatmeme-Printer/issues/10) and [this thread](http://gbatemp.net/threads/how-to-use-shinyquagsires-splatoon-2-post-printer.479497/) on GBAtemp for more information. (Note for Mac users - the AVR MacPack is now called AVR CrossPack. If that does not work, you can try installing `avr-gcc` with `brew`.)

Depending on which hardware you use, you should edit the makefile line number 15, "MCU".

LUFA has been included as a git submodule, so cloning the repo like this:

```
git clone --recursive git@github.com:bertrandom/snowball-thrower.git
```

will put LUFA in the right directory.

Now you should be ready to rock. Open a terminal window in the `snowball-thrower` directory, type `make`, and hit enter to compile. If all goes well, the printout in the terminal will let you know it finished the build! Follow the directions on flashing `Joystick.hex` onto your Teensy, which can be found page where you downloaded the Teensy Loader application.

#### Thanks

Thanks to Shiny Quagsire for his [Splatoon post printer](https://github.com/shinyquagsire23/Switch-Fightstick) and progmem for his [original discovery](https://github.com/progmem/Switch-Fightstick).

Thanks to [exsilium](https://github.com/bertrandom/snowball-thrower/pull/1) for improving the command structure, optimizing the waiting times, and handling the failure scenarios. It can now run indefinitely!

Thanks to Bertrandom for his [Snowball Thrower](https://github.com/bertrandom/snowball-thrower). This provided a template for creating custom input scripts.