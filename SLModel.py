import os.path
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.callbacks import ModelCheckpoint
from keras.optimizers import RMSprop
from keras.models import h5py
import numpy as np

features = None
labels = None
if os.path.isfile('train_data.npz'):
    print('File exists, loading...')
    features = np.load('train_data.npz')['data']
    labels = np.load('train_label.npz')['data']
    print('Data loaded.')
else:
    trainDataPath = './dataset/dataset_gomocup15/train.txt'
    testDataPath = './dataset/dataset_gomocup15/test.txt'
    validationDataPath = './dataset/dataset_gomocup15/validation.txt'

    fileList = [trainDataPath,testDataPath,validationDataPath]

    features = np.zeros((1,225))
    labels = np.zeros((1,225))

    items = 0

    for fileName in fileList:

        f = open(fileName)

        print('Proccessing file ' + fileName +', waiting... ')

        for lines in f:
            chessboard = lines.split(',')[:225]
            rest = lines.split(',')[225:]

            feature = np.zeros((1,225))
            label = np.zeros((1,225))

            for i in range(225):
                feature[0][i] = int(chessboard[i])
                if int(rest[i * 2]) == 0:
                    label[0][i] = 0
                else:
                    label[0][i] = int(rest[i * 2 + 1]) * 1.0 / int(rest[i * 2])
            label = label / np.sum(label)

            features = np.vstack((features,feature))
            labels = np.vstack((labels,label))

            items += 1
            if items % 5000 == 0:
                print(str(items) + ' data items procceed...')

    features = features[1:,:]
    labels = labels[1:,:]
    np.savez('train_data.npz', data = features)
    np.savez('train_label.npz', data = labels)
    print('Data saved.')

features = features.reshape((-1,15,15,1))
# labels = labels.reshape(labels.shape[0],225)

model = Sequential()
model.add(Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same',
                 activation ='relu', input_shape = (15,15,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same',
                 activation ='relu', input_shape = (15,15,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same',
                 activation ='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(225, activation = "softmax"))

optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

model.compile(optimizer = optimizer , loss = "categorical_crossentropy", metrics=["accuracy"])
checkpoint = ModelCheckpoint(filepath = 'pre_knowledge.model' , verbose = 1, save_best_only = True)
model.fit(features, labels, epochs = 10, batch_size = 64, validation_split = 0.1, callbacks = [checkpoint])
