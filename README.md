# Emerging-Technologies-Project-Year4
> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr Ian McLoughlin  
> Project 2017 : [Web Application in Python to Recognise Digits in Images](https://github.com/w326004741/Emerging-Technologies-Project-Year4/wiki/Project-2017) 

> Student: [Weichen Wang](https://github.com/w326004741)

The following are your instructions to complete the project for the module Emerging Technologies for 2017.

## Overview
In this project I created a web application in Python to recognise digits in images. You could be able to visit the web application through your browser, `Draw`an image containing a single digit, and the web application could respond with the digit contained in the image. 

## How to create web appliction:
A minimal [Flask](http://flask.pocoo.org/) application looks something like this:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```
Just save it as hello.py or anyname.py. 
- Open your Terminal(for Mac), cmd(for windows).
- Into the folder with hello.py file.
```
$ export FLASK_APP=hello.py
$ flask run
* Running on http://127.0.0.1:5000/
```
Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting.

## You need to install before use:
- [Python 2.7](https://www.python.org/downloads/) or [Python 3.x](https://www.python.org/downloads/)
- [Flask](http://flask.pocoo.org/)
- [Tensorflow](https://www.tensorflow.org/install/)
- [Keras](https://keras.io/#installation)
- [Numpy](http://www.numpy.org/)
- [Scipy](https://www.scipy.org/install.html)
- [Pillow](https://pillow.readthedocs.io/en/4.3.x/installation.html)
- [Jinja2](http://flask.pocoo.org/docs/0.12/templating/)

Use pip to install [Flask](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application): 
- `$ pip install Flask`

Use pip to install [Tensorflow](https://www.tensorflow.org/install/): 
- `$ pip install tensorflow`
- `$ pip3 install tensorflow`

Use pip to install [Keras](https://keras.io/#installation):
- `pip install keras`

Use pip to install [Numpy](https://docs.scipy.org/doc/numpy-1.10.0/user/install.html):
- `pip install numpy`

Use pip to install [Scipy](https://stackoverflow.com/questions/2213551/installing-scipy-with-pip):
- `pip install scipy`

Use pip to install [Pillow](https://pillow.readthedocs.io/en/4.3.x/installation.html):
- `$ pip install Pillow`

Use pip to install [Jinja2](https://stackoverflow.com/questions/6726983/jinja-install-for-python)
- `pip install Jinja2`
## How to use this repository:
1. Click Clone or download and Copy to clipboard
2. Enter your Terminal(for mac) or cmd(for windows), and following below:
```
# Change directory to anywhere just you like put
cd anywhere.....

# Clone this repository
git clone https://github.com/w326004741/Emerging-Technologies-Project-Year4.git
&
cd your folder(Emerging-Technologies-Project-Year4)

# You can run webapp.py file:
export FLASK_APP=webapp.py
flask run
```
## About Project:
Have three .py files : webapp.py, train.py, load.py
```
 webapp.py : Run web application in Python

 train.py :  1. Complete split the data into training and testing
             2. Train the MNIST model
             3. Test the MNIST model
             4. Save the model to h5 file for later use
         
 load.py : 1. Load model from h5 file.
           2. Using tf.get_default_graph(), We need to use the tf.get_default_graph () command to get the graph.
              Because of he default graph lives in the _default_graph_stack, but we don't have access to that directly.
 
```
## Reference:
- [tf.get_default_graph()](https://www.tensorflow.org/api_docs/python/tf/get_default_graph)
- [How to use css file in html](https://stackoverflow.com/questions/16351826/link-to-flask-static-files-with-url-for)
- [re.search()](https://stackoverflow.com/questions/20240239/python-re-search)
- [reshape()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)
- [jquery-3.2.0.min.js](http://blog.jquery.com/2017/03/16/jquery-3-2-0-is-out/)
- [Keras backend](https://keras.io/backend/)
- [to_categorical](https://keras.io/utils/#to_categorical)
- [Convolutional Neural Network(CNN)](http://cs231n.github.io/convolutional-networks/)
- [CNN Youtube Google](https://www.youtube.com/watch?v=jajksuQW4mc)
- [CNN Youtube Morvan Tutorial](https://www.youtube.com/watch?v=JCBe_yjDmY8)
- [Conv2D](https://keras.io/layers/convolutional/#conv2d)
- [MaxPooling](https://keras.io/layers/pooling/)
- [Dropout](https://keras.io/layers/core/#dropout)
- [Optimizer Adadelta](https://keras.io/optimizers/#adadelta)
- [channels_first & channels_last](http://blog.csdn.net/sinat_26917383/article/details/72859145)
- [HTML form Using JQuery AJAX](https://stackoverflow.com/questions/16323360/submitting-html-form-using-jquery-ajax)
- [Loading jQuery](http://flask.pocoo.org/docs/0.12/patterns/jquery/)
- [Jinja2](http://flask.pocoo.org/docs/0.12/templating/)
- [Set Script Root](http://flask.pocoo.org/docs/0.12/patterns/jquery/)
