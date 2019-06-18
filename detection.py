"""Run.py

    This file contains the required methods to run the trained machine learning algorithm on the picamera to detect waves
    and water the raspberry pi
"""

from sys import argv, stderr, exit
from os import getenv

import numpy as np
from tensorflow import keras

from camera import Camera
from pinet import PiNet
from motor import motor_main
from sensors import get_needs_water

SMOOTH_FACTOR = 0.8


def detection_main():

    print("starting wave detection")

    if get_needs_water() == True:

        print("plant needs water, watching camera feed")
        model_file = argv[1]

        # We use the same MobileNet as during recording to turn images into features
        print('Loading feature extractor')

        extractor = PiNet()

        # Here we load our trained classifier that turns features into categories
        print('Loading classifier')
        classifier = keras.models.load_model(model_file)

        # Initialize the camera and sound systems
        camera = Camera(training_mode=False)
        random_sound = RandomSound()


        # Smooth the predictions to avoid interruptions to audio
        smoothed = np.ones(classifier.output_shape[1:])
        smoothed /= len(smoothed)

        print('watching')
        while True:
            raw_frame = camera.next_frame()

            # Use MobileNet to get the features for this frame
            z = extractor.features(raw_frame)

            # With these features we can predict a 'normal' / 'yeah' class (0 or 1)
            # Keras expects an array of inputs and produces an array of outputs
            classes = classifier.predict(np.array([z]))[0]

            # smooth the outputs - this adds latency but reduces interruptions
            smoothed = smoothed * SMOOTH_FACTOR + classes * (1.0 - SMOOTH_FACTOR)
            selected = np.argmax(smoothed) # The selected class is the one with highest probability

            # Show the class probabilities and selected class
            summary = 'Class %d [%s]' % (selected, ' '.join('%02.0f%%' % (99 * p) for p in smoothed))
            stderr.write('\r' + summary)

            # Perform actions for selected class. In this case, play a sound from the sounds/ dir
            if selected == 0:
                print("wave detected, running pump")
                motor_main()
                break
            else:
                continue
    return
