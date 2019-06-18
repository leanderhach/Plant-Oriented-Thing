import io
import os
import picamera
import time
from datetime import datetime
from PIL import Image

camera = 0
difference = 0
pxels = 0
width = 0
height = 0


def setup_camera():
    global camera, difference, pixels, width, height
    
    camera = picamera.PiCamera()

    difference = 10
    pixels = 25

    width = 1280
    height = 960

def compare():
    global camera
    
    camera.resolution = (100, 75)
    stream = io.BytesIO()
    camera.capture(stream, format = "bmp") 
    stream.seek(0)
    im = Image.open(stream)
    buffer = im.load()
    stream.close()
    return im, buffer

def newimage():
    global camera, width, height
    
    time = datetime.now()
    filename = "motion-%04d%02d%02d-%02d%02d%02d.jpg" % (time.year, time.month, time.day, time.hour, time.minute, time.second)
    camera.resolution = (width, height)
    camera.capture(filename)
    print("Captured {}".format(filename))

    image1, buffer1 = compare()

    timestamp = time.time()

while (True):
    setup_camera()
    image2, buffer2 = compare()

    changedpixels = 0
    for x in range(0, 100):
        for y in range(0, 75):
            pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
            if pixdiff > difference:
                changedpixels += 1

    if changedpixels > pixels:
        timestamp = time.time()
        newimage(width, height)

    image1 = image2
    buffer1 = buffer2
