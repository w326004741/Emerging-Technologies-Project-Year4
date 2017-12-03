import os
from scipy.misc import imsave, imread, imresize
from flask import Flask, render_template, request
import keras.models
import re
import base64
import sys 
sys.path.append(os.path.abspath("./model")) # Must be before load import * （必须在 from load import * 之前）
from load import * # 引用 load.py内的所有东西
import numpy as np

app = Flask(__name__)
global model, graph
model, graph = init()
    
@app.route('/')
def index():
    return render_template("index.html")

def parseImage(imgData):
    # parse canvas bytes and save as output.png
     # 将base64编码的解码保存图片
    # re: Support for regular expressions 支持正则表达式
    #  re.search(pattern, string, flags)
    # 用re.search()找出所有base64模式的数据。
    # https://stackoverflow.com/questions/20240239/python-re-search
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

@app.route('/predict/', methods=['GET','POST'])
def predict():
    # get data from drawing canvas and save as image
    parseImage(request.get_data())

    # read parsed image back in 8-bit, black and white mode (L)
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))
    # reshape image data for use in neural network
    # 重塑图像数据用于神经网络
    # 给数组赋予新的形状而不改变其数据
    # Gives a new shape to an array without changing its data.
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
    # reshape(dimension(维度)，28*28＝784的pixel，1＝black黑色)
    x = x.reshape(1,28,28,1)
    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out, axis=1))
        response = np.array_str(np.argmax(out, axis=1))
        return response 
    


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)