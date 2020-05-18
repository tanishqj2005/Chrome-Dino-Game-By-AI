# Importing Required Modules:

from PIL import Image, ImageGrab
import numpy as np
from numpy import asarray
import time
import pickle
import keyboard 
import math
from sklearn.linear_model import LogisticRegression

# Writing some essential functions:

def whichKey():
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('down'):  # if key 'q' is pressed 
            print('1')
            return 1
        elif keyboard.is_pressed('up'):
            print('2')
            return 2
        elif keyboard.is_pressed('q'):
            print('3')
            return 3
        else:
            print('0')
            return 0
    except:
        print('error!')

# Defining the model:

# file = open('model.pkl','rb')
# clf=pickle.load(file)
# file.close()
# clf = LogisticRegression()


# Writing the code for training the model:

if __name__ == "__main__":
    # clf = LogisticRegression()
    file = open('model.pkl','rb')
    clf=pickle.load(file)
    file.close()
    x = []
    y = []
    print('Game starting in 2 seconds...')
    time.sleep(2)
    while True:
        key = whichKey()
        if key == 3:
            break
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
        x.append(flatten_image)
        y.append(key)
    X = np.array(x)
    Y = np.array(y)
    no_of_images = X.shape[0]
    batch_size = 20
    iterations = int(math.floor(no_of_images/batch_size))
    for i in range(iterations):
        start = i*batch_size
        end = (i+1)*batch_size
        X_minibatch = X[start:end,:]
        print(X_minibatch.shape)
        Y_minibatch = Y[start:end]
        print(Y_minibatch.shape)
        clf.fit(X_minibatch,Y_minibatch)

    #open a file where you want to store the data:
    file = open('model.pkl','wb')

    #dump info into that file:
    pickle.dump(clf,file)
    file.close()
