from __future__ import print_function
import keras as kr
import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
# https://keras.io/backend/ backend可兼容不同的后台(Theano th / Tensorflow tf)
from keras import backend as K
import json

# the data, shuffled and split between train and test sets
# /Users/weichenwang/anaconda/lib/python3.6/site-packages/keras/datasets
# 自动在线加载 MNIST datasets,默认路径为：local path:  '~/.keras/datasets/' + path
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 返回默认图像数据格式约定（'channels_first'或'channels_last'）。
# http://blog.csdn.net/sinat_26917383/article/details/72859145
# channels_first = Theano(3, 128, 128)), channels_last = Tensorflow(128, 128, 3)).
if K.image_data_format() == 'channels_first':
    # reshape(维度，28*28＝784的pixel，1＝black黑色)
    # reshape(dimension，b, img_rows, img_cols)
    x_train = x_train.reshape(x_train.shape[0], 1, 28, 28)
    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28)
    input_shape = (1, 28, 28)
else: # channel_last: Tensorflow tf
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
# 对训练和测试数据处理，转为float
# Processing and testing of data processing, converted to float
# 对数据进行归一化到0-1 因为图像数据最大是255
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
print(x_train.shape, 'x_train shape:')
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
# Outputs: 60000, 28, 28, 1) x_train shape
# 60000 train sample
# 10000 test sample   在线下载完成，打印输出下载数据。

# Converts a class vector (integers) to binary class matrix.
# 将一个类向量（整数）转换为二进制类矩阵。
# 因为keras要求格式为binary class matrices，所以需要转化被binary
# https://keras.io/utils/#to_categorical
# num_classes：类的总数
# 解压后可以查看一下代码文件所在的文件夹中会有两个文件夹not_MNIST_large和not_MNIST_small，large用来训练，small用来验证，每个文件夹中都有10个文件夹，分别保存了A到J的图像(28*28)，这些图像就是数据集，标签就是A到J，当然之前下载的压缩文件也在

# keras.utils.to_categorical(y, num_classes=None), num_classes=10
y_train = kr.utils.to_categorical(y_train, 10)
y_test = kr.utils.to_categorical(y_test, 10)

# Create a neural nerwork
# keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
# https://keras.io/layers/convolutional/#conv2d
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
    Conv2D(64, kernel_size=(3,3), activation='relu'),
    # MaxPooling: https://keras.io/layers/pooling/
    MaxPooling2D(pool_size=(2, 2)), # Max pooling operation for spatial data.取2x2＝4个pixel大小的值
    Dropout(0.25), # dropout prevent overfitting 防止过拟合，学习程度太高
    Flatten(), # Flattens the input. Does not affect the batch size.把分开的集合组合在一起: [1,2][3,4]->[1,2,3,4]
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# https://keras.io/optimizers/#adadelta
model.compile(optimizer="adadelta", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=60, batch_size=32, verbose=1, validation_data=(x_test,y_test))
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print("\n Final test set Loss:      %6.6f" % (loss))
print("\n Final test set Accuracy:      %6.6f" % (accuracy))

# save the model to h5 file for later use.
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
with open('model.json', 'w') as outfile:
    json.dump(model.to_json(), outfile)
model.save_weights('weights.h5')