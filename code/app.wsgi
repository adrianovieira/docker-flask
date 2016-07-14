# -*- coding: utf-8 -*-
import os, time
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Hello, World of Flask on Docker!" + \
           "<br /><small>"+time.strftime("%d/%h/%Y %H:%M:%S") + \
           "<br />@" + os.uname()[1] + \
           "<br />Hosted on: " + ' '.join(os.uname()) + \
           "</small>"
