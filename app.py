#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method =='POST':
        uploaded_file = request.files['file']
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
