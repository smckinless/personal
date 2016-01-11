from flask import Flask, render_template, request, redirect, url_for, session, abort
from werkzeug.utils import secure_filename
import jinja2
import os
import json
import re
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()