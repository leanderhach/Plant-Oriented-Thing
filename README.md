# Plant-Oriented-Thing

Welcome to the public repository for the P.O.T. project. 

## What is this?

The P.O.T. is a 'smart pot' designed for the Maker Lab course of the University Of Bolzano.

## What can it do?

It monitors the humidity in the plant's soil and asks the user to wave at to activate a pump to water the plant. On top of that, it adjustes a LED strip to provide the plant with the necessary light for a constant day-night cycle; if the plant needs to be watered, the led strip turns of a selected warning color.

The color of the leds and the plant can be selected from an online app. One page of the app can be accessed to show just plant information. It can be useful for info screens for the P.O.T.

## Where do you gather the data of the plant?

We download and save the data periodically by Trefle, an online open API.

## How do you detect a wave?

We used a trained AI written with Tensorflow to detect the wave.

## The leds do not close at night.

This is a prototype. That'll be for V2.

## OMG the code is ugly

Hush! It's wonderful.

## How do i set it up?

You require a Raspberry Pi with Raspbian and an Explorer Hat to run this program.

Instructions for running this program locally

1. Check if pip is installed by typing pip into a cmd window. If an error occurs, install pip

2. type the following command: ```pip install virtualenv```

3. open a new cmd window in the folder where you have this project. For example: ```C:\users\leand\POT```

4. type the following command:  ```virtualenv env```

    4a. On windows, type ```.\env\Scripts\activate```

    4b. on mac, type ```source env/bin/activate```

5. type ```pip install -r requirements.txt```
   
## Good, how do i run it?

Navigate to ```/home/pi/github/POT``` and execute this command:

```
env "PATH=$PATH" python3 main.py
```




