# Importing Required Modules:

from PIL import Image, ImageGrab
import numpy as np
from numpy import asarray
import time
import pickle
import pyautogui
import keyboard 

# Writing some essential functions:

def hit(key):
    pyautogui.keyDown(key)
    return

def whichKey():
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):
            print('Quitting Game...')
            return 3
    except:
        pass

# Defining the model:

file = open('model.pkl','rb')
clf=pickle.load(file)
file.close()

# Writing the code for using the trained model to play the game:

if __name__ == "__main__":
    print('Game starting in 2 seconds...')
    time.sleep(2)
    while True:
        if(whichKey() == 3):
            break
        else:
            flatten_image = []
            image = ImageGrab.grab().convert('L')
            width, height = image.size
            left = 0
            top = int(2*height / 7)
            right = 300
            bottom = int(4 * height / 7)
            image = image.crop((left, top, right, bottom))
            data = asarray(image) 
            for i in data:
                for j in i:
                    flatten_image.append(j)
            flatten_image= np.array(flatten_image)
            x = np.array([flatten_image])
            model_prediction = clf.predict(x)[0]
            print(model_prediction)
            if model_prediction ==1:
                hit("down")

            elif model_prediction == 2:
                hit("up")
    print('Thanks for playing the game :)')
