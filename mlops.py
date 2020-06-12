{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:516: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint8 = np.dtype([(\"qint8\", np.int8, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:517: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint8 = np.dtype([(\"quint8\", np.uint8, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:518: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint16 = np.dtype([(\"qint16\", np.int16, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:519: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint16 = np.dtype([(\"quint16\", np.uint16, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:520: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint32 = np.dtype([(\"qint32\", np.int32, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:525: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  np_resource = np.dtype([(\"resource\", np.ubyte, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:541: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint8 = np.dtype([(\"qint8\", np.int8, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:542: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint8 = np.dtype([(\"quint8\", np.uint8, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:543: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint16 = np.dtype([(\"qint16\", np.int16, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:544: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint16 = np.dtype([(\"quint16\", np.uint16, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:545: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint32 = np.dtype([(\"qint32\", np.int32, 1)])\n",
      "C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:550: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  np_resource = np.dtype([(\"resource\", np.ubyte, 1)])\n"
     ]
    }
   ],
   "source": [
    "from keras.datasets import mnist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = mnist.load_data('mymnist.db')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "train , test = dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train , y_train = train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000, 28, 28)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test , y_test = test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10000, 28, 28)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "img1 = X_train[8]\n",
    "img2 = X_train[2]\n",
    "img3 = X_train[2001]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c14a33af48>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow(img1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train[8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c14a3eff48>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow(img2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c14a465648>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow(img3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train[2001]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28, 28)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img1.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(784,)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eimg = img1.reshape(28*28)\n",
    "eimg.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_1d = X_train.reshape(-1 , 28*28)\n",
    "X_test_1d = X_test.reshape(-1 , 28*28)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000, 784)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_1d.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = X_train_1d.astype('float32')\n",
    "X_test = X_test_1d.astype('float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000, 784)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000,)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.utils.np_utils import to_categorical"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_train = to_categorical(y_train)\n",
    "y_test = to_categorical(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., ..., 0., 0., 0.],\n",
       "       [1., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 1., 0.]], dtype=float32)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.models import Sequential"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.layers import Dense"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "dense_1 (Dense)              (None, 256)               200960    \n",
      "=================================================================\n",
      "Total params: 200,960\n",
      "Trainable params: 200,960\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.add(Dense(units=256,input_dim = 28*28 , activation='relu'))\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "dense_1 (Dense)              (None, 256)               200960    \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 128)               32896     \n",
      "=================================================================\n",
      "Total params: 233,856\n",
      "Trainable params: 233,856\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.add(Dense(units=128,input_dim = 28*28, activation='relu'))\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Dense(units= 32, input_dim = 28*28,activation='relu'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "dense_1 (Dense)              (None, 256)               200960    \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 128)               32896     \n",
      "_________________________________________________________________\n",
      "dense_3 (Dense)              (None, 32)                4128      \n",
      "=================================================================\n",
      "Total params: 237,984\n",
      "Trainable params: 237,984\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "dense_1 (Dense)              (None, 256)               200960    \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 128)               32896     \n",
      "_________________________________________________________________\n",
      "dense_3 (Dense)              (None, 32)                4128      \n",
      "_________________________________________________________________\n",
      "dense_4 (Dense)              (None, 10)                330       \n",
      "=================================================================\n",
      "Total params: 238,314\n",
      "Trainable params: 238,314\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.add(Dense(units=10,input_dim = 28*28, activation='softmax'))\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "dense_1 (Dense)              (None, 256)               200960    \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 128)               32896     \n",
      "_________________________________________________________________\n",
      "dense_3 (Dense)              (None, 32)                4128      \n",
      "_________________________________________________________________\n",
      "dense_4 (Dense)              (None, 10)                330       \n",
      "=================================================================\n",
      "Total params: 238,314\n",
      "Trainable params: 238,314\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.optimizers import Adam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(optimizer=\"Adam\", loss='categorical_crossentropy', metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\ADITI\\anaconda3\\lib\\site-packages\\keras\\backend\\tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.\n",
      "\n",
      "Epoch 1/25\n",
      "60000/60000 [==============================] - 11s 178us/step - loss: 1.6500 - accuracy: 0.4798\n",
      "Epoch 2/25\n",
      "60000/60000 [==============================] - 11s 184us/step - loss: 0.6384 - accuracy: 0.8055\n",
      "Epoch 3/25\n",
      "60000/60000 [==============================] - 10s 171us/step - loss: 0.2513 - accuracy: 0.9380\n",
      "Epoch 4/25\n",
      "60000/60000 [==============================] - 10s 166us/step - loss: 0.1587 - accuracy: 0.9563\n",
      "Epoch 5/25\n",
      "60000/60000 [==============================] - 10s 159us/step - loss: 0.1247 - accuracy: 0.9656\n",
      "Epoch 6/25\n",
      "60000/60000 [==============================] - 10s 160us/step - loss: 0.1051 - accuracy: 0.9715\n",
      "Epoch 7/25\n",
      "60000/60000 [==============================] - 11s 175us/step - loss: 0.0864 - accuracy: 0.9757\n",
      "Epoch 8/25\n",
      "60000/60000 [==============================] - 10s 159us/step - loss: 0.0762 - accuracy: 0.9786\n",
      "Epoch 9/25\n",
      "60000/60000 [==============================] - 10s 163us/step - loss: 0.0714 - accuracy: 0.9808\n",
      "Epoch 10/25\n",
      "60000/60000 [==============================] - 10s 160us/step - loss: 0.0655 - accuracy: 0.9824\n",
      "Epoch 11/25\n",
      "60000/60000 [==============================] - 10s 160us/step - loss: 0.0610 - accuracy: 0.9843\n",
      "Epoch 12/25\n",
      "60000/60000 [==============================] - 10s 164us/step - loss: 0.0591 - accuracy: 0.9851\n",
      "Epoch 13/25\n",
      "60000/60000 [==============================] - 10s 164us/step - loss: 0.0521 - accuracy: 0.9860\n",
      "Epoch 14/25\n",
      "60000/60000 [==============================] - 10s 165us/step - loss: 0.0510 - accuracy: 0.9873\n",
      "Epoch 15/25\n",
      "60000/60000 [==============================] - 10s 166us/step - loss: 0.0438 - accuracy: 0.9886\n",
      "Epoch 16/25\n",
      "60000/60000 [==============================] - 10s 160us/step - loss: 0.0475 - accuracy: 0.9882\n",
      "Epoch 17/25\n",
      "60000/60000 [==============================] - 10s 161us/step - loss: 0.0494 - accuracy: 0.9890s - loss: 0.049\n",
      "Epoch 18/25\n",
      "60000/60000 [==============================] - 10s 161us/step - loss: 0.0432 - accuracy: 0.9892\n",
      "Epoch 19/25\n",
      "60000/60000 [==============================] - 10s 175us/step - loss: 0.0393 - accuracy: 0.9906\n",
      "Epoch 20/25\n",
      "60000/60000 [==============================] - 11s 187us/step - loss: 0.0409 - accuracy: 0.9905\n",
      "Epoch 21/25\n",
      "60000/60000 [==============================] - 11s 185us/step - loss: 0.0435 - accuracy: 0.9902\n",
      "Epoch 22/25\n",
      "60000/60000 [==============================] - 10s 162us/step - loss: 0.0341 - accuracy: 0.9919\n",
      "Epoch 23/25\n",
      "60000/60000 [==============================] - 10s 161us/step - loss: 0.0422 - accuracy: 0.9908\n",
      "Epoch 24/25\n",
      "60000/60000 [==============================] - 10s 161us/step - loss: 0.0394 - accuracy: 0.9911\n",
      "Epoch 25/25\n",
      "60000/60000 [==============================] - 10s 161us/step - loss: 0.0405 - accuracy: 0.9911\n"
     ]
    }
   ],
   "source": [
    "fit_model= model.fit(X_train, y_train, epochs=25)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.save(\"accuracy.pk1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = X_test[3].transpose()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "if (X_test[6].ndim ==1):XpredictInputData = np.array([X_test[6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = model.predict(XpredictInputData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c158fb0e88>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAABECAYAAACCuY6+AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAGmklEQVR4nO3dW4xdVR3H8e/PKVYLqRQxsRdiISrSeKtMBG1CDKVRoikPalISDRhJYyKCxMRr4oNP1RgvD8akFg1RgiQj0Woa0KbwZNIwQL1ALdRqaG2VAgVBIzD68+HscU5OZzoz3Xtm1bN+n2Qy+5y9Zq9/Vs75zZk156wl20RExPB7WekCIiJicSTwIyIqkcCPiKhEAj8iohIJ/IiISiTwIyIq0SrwJZ0n6VeSHmu+r5ih3b8l7Wu+drbpMyIiTo/avA9f0teAp21vk/R5YIXtz03T7nnb57SoMyIiWmob+AeA99g+JmklcJ/ti6dpl8CPiCisbeA/Y/vcvtsnbJ80rSNpAtgHTADbbP90huttBbYCjDBy6TKWn3ZtMZze+NZ/li6BR3+7rHQJETN6jhNP2n7NdOdmDXxJu4HXTnPqS8Btcwz8VbaPSroI2ANstP3HU/W7XOf5Mm08ZW1Rn3uO7itdAu9d9fbSJUTMaLfHHrA9Ot25JbP9sO2rZjon6W+SVvZN6TwxwzWONt8PSboPWA+cMvAjIqJbbd+WuRO4rjm+DvjZYANJKyQtbY7PBzYAj7TsNyIi5qlt4G8DNkl6DNjU3EbSqKQdTZtLgHFJvwHupTeHn8CPiFhks07pnIrtp4CTJtptjwM3NMe/Bt7Spp+IiGgvn7SNiKhEAj8iohIJ/IiISiTwIyIqkcCPiKhEAj8iohIJ/IiISiTwIyIq0UngS3qfpAOSDjbr4g+eXyrpzub8Xklru+g3IiLmrnXgSxoBvgNcDawDrpW0bqDZx4ETtl8PfBP4att+IyJifrp4hf9O4KDtQ7ZfBH4MXDPQ5hrgtuZ4DNgoSR30HRERc9RF4K8GDvfdPtLcN20b2xPAs8CrBy8kaaukcUnjL/FCB6VFRMSkLgJ/ulfqg7uqzKUNtrfbHrU9ehZLOygtIiImdRH4R4AL+m6vAY7O1EbSEuBVwNMd9B0REXPUReDfD7xB0oWSXg5sobcxSr/+jVI+BOxxm810IyJi3lqthw+9OXlJNwL3ACPA920/LOkrwLjtncCtwA8lHaT3yn5L234jImJ+Wgc+gO1dwK6B+77cd/wv4MNd9BUREacnn7SNiKhEAj8iohIJ/IiISiTwIyIqkcCPiKhEAj8iohIJ/IiISiTwIyIqsVgboFwv6bikfc3XDV30GxERc9f6k7Z9G6BsordI2v2Sdtp+ZKDpnbZvbNtfREScnsXaACUiIgrrYi2d6TZAuWyadh+UdAXwKHCL7cODDSRtBbY2N5/f7bEDLWs7H3iy5TWGxVCMxcjKTi7TciwOdlLEGWIoHhcdGZaxeN1MJ7oI/LlsbvJz4A7bL0j6BL3tDq886Yfs7cD2DmrqFSaN2x7t6nr/zzIWUzIWUzIWU2oYi0XZAMX2U7Yn9yz8HnBpB/1GRMQ8LMoGKJL6/xDfDOzvoN+IiJiHxdoA5SZJm4EJehugXN+23znqbHpoCGQspmQspmQspgz9WCg7DUZE1CGftI2IqEQCPyKiEkMb+LMt91ALSRdIulfSfkkPS7q5dE0lSRqR9JCkX5SupTRJ50oak/SH5vHxrtI1lSLplub58XtJd0h6RemaFsJQBn7fcg9XA+uAayWtK1tVMRPAZ2xfAlwOfLLisQC4mbxLbNK3gbttvwl4G5WOi6TVwE3AqO0303vzyZayVS2MoQx8stzD/9g+ZvvB5vg5ek/q1WWrKkPSGuD9wI7StZQmaTlwBXArgO0XbT9TtqqilgCvlLQEWMbAZ4mGxbAG/nTLPVQZcv0krQXWA3vLVlLMt4DPAv8pXcgZ4CLgOPCDZoprh6SzSxdVgu2/AF8HHgeOAc/a/mXZqhbGsAb+XJZ7qIqkc4CfAJ+2/ffS9Sw2SR8AnrD9QOlazhBLgHcA37W9HvgHUOX/uiStoDcDcCGwCjhb0kfKVrUwhjXwZ13uoSaSzqIX9rfbvqt0PYVsADZL+jO9Kb4rJf2obElFHQGO2J78a2+M3i+AGl0F/Mn2cdsvAXcB7y5c04IY1sCfdbmHWkgSvXna/ba/UbqeUmx/wfYa22vpPR722B7KV3FzYfuvwGFJFzd3bQQG97CoxePA5ZKWNc+XjQzpP7C7WC3zjDPTcg+FyyplA/BR4HeS9jX3fdH2roI1xZnhU8DtzYuiQ8DHCtdThO29ksaAB+m9q+0hhnSZhSytEBFRiWGd0omIiAEJ/IiISiTwIyIqkcCPiKhEAj8iohIJ/IiISiTwIyIq8V9IgBlQyDJK1wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c15a037908>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow([y_test[6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
