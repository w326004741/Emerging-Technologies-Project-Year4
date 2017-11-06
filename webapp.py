# Adapted from: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
# 我使用一个“templates”目录和一个“static”目录。我将所有的.html文件/Flask模板放在templates目录中，而static包含CSS/JS.
# render_template对通用的html文件工作正常.
import os
from flask import Flask, request, redirect, url_for, render_template #add render_template
from werkzeug.utils import secure_filename

# change the path
UPLOAD_FOLDER = '/Users/weichenwang/Year4/Ian/Emerging-Technologies-Project-Year4/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template("index.html") # use render_templated

@app.route('/uploaded_file')
def uploaded_file():
    return 'Upload Successful'