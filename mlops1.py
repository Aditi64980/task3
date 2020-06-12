from keras.datasets import mnist
dataset = mnist.load_data('mymnist.db')
len(dataset)
train , test = dataset
len(train)
len(test)
X_train , y_train = train
X_train.shape
X_test , y_test = test
X_test.shape
import matplotlib.pyplot as plt
img1 = X_train[8]
img2 = X_train[2]
img3 = X_train[2001]
plt.imshow(img1)
y_train[8]
plt.imshow(img2)
y_train[2]
plt.imshow(img3)
y_train[2001]
img1.shape
eimg = img1.reshape(28*28)
eimg.shape
eimg = img1.reshape(28*28)
eimg.shape
X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)
X_train_1d.shape
X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')
X_train.shape
y_train.shape
from keras.utils.np_utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
y_train
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=256,input_dim = 28*28 , activation='relu'))
model.summary()
model.add(Dense(units= 32, input_dim = 28*28,activation='relu'))
model.summary()
model.add(Dense(units=10,input_dim = 28*28, activation='softmax'))
model.summary()
model.summary()
from keras.optimizers import Adam
model.compile(optimizer="Adam", loss='categorical_crossentropy', metrics=['accuracy'])
fit_model= model.fit(X_train, y_train, epochs=25)
model.save("accuracy.pk1")
img = X_test[3].transpose()
import numpy as np
if (X_test[6].ndim ==1):XpredictInputData = np.array([X_test[6]])
img = model.predict(XpredictInputData)
plt.imshow(img)
plt.imshow([y_test[6]])

