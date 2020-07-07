# enhancemainwindowthemes
Themes for the anki addon enhance main window

![preview](enhancemainwindow/magenta_s.png)
![preview](enhancemainwindow/ice_e.png)

For more screenshots see the enhancemainwindow directory.

## Installing
If you don't want to change any settings, just open up the json file for the config you'd like. For example pinky_extended.json, copy all of it's content and open up anki. Click on Tools -> Addons -> Enhance Main Window -> Config

Delete all of the existing config in here (If you have made any changes, make sure to make a backup first) and paste the new config. Now restart anki and you should be good to go. If you encounter any difficulties, open an issue on [this github repository](https://github.com/b3nj5m1n/enhancemainwindowthemes).

## Auto applying a new config (Ignore unless you're using pywal or something of the sort)
There is no working implementation of this in this repo. It is however possible. The config is stored in the addon directory in the file meta.json. You can easily modify this file. I do it using my scripts on my setup, if you're interested, have a look at my [dotfiles](https://github.com/b3nj5m1n/enhancemainwindowthemes) (Especially the bay scripts).

## Templates
In this repo you will find 2 templates, these contain the corresponding config file, instead of actual colors there are placeholder which will be overwritten by the python script.

## colorschemes.json
This json file contains all of the color defenitions for all of the color schemes.

## Python Script
You can execute the python script with the name of a colorscheme as the first argument to update the file. Do this if you have changed settings in the template or colors in the colorschemes.json
```
# If you're on an arch based system; If you only have python3.x installed
python parser.py "pinky"
# If python still defaults to python2 on your os
python3 parser.py "pinky"
```

## Makefile
Running `make` will run the parser on all colorschemes.
