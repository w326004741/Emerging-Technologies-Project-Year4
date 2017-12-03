import numpy as np
import keras.models
import keras as kr
from scipy.misc import imread, imresize,imshow
import tensorflow as tf
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

def init():
    input_shape = (28, 28, 1)
    model = Sequential([
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
        Conv2D(64, kernel_size=(3,3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)), # 取2x2＝4个pixel大小的值
        Dropout(0.25), # dropout prevent overfitting 防止过拟合，学习程度太高
        Flatten(), # Flattens the input. Does not affect the batch size.把分开的集合组合在一起: [1,2][3,4]->[1,2,3,4]
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
        ])
    
    #load woeights into new model
    model.load_weights("weights.h5")
    print("--------------loaded model from h5 file--------------------")

    #compile and evaluate loaded model
    model.compile(optimizer="adadelta", loss="categorical_crossentropy", metrics=["accuracy"])
# 当我们导入tensorflow包的时候，系统已经帮助我们产生了一个默认的图，它被存在_default_graph_stack中，但是我们没有权限直接进入这个图，我们需要使用tf.get_default_graph()命令来获取图。
# the default graph lives in the _default_graph_stack, but we don't have access to that directly. We use tf.get_default_graph().
# get_default_graph: http://www.jianshu.com/p/5080d45d39da
    graph = tf.get_default_graph()
    return model, graph
print("----------------loaded-------------------")