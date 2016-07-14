# coding: utf-8
'''
Application: flask_kafka
Modulue: main
description: Tasting docker, redis, kafka
author: Adriano dos Santos Vieira <adriano.svieira at google.com>
character encoding: UTF-8
'''
import os, time
from flask import Flask
from flask import render_template

application = Flask(__name__, template_folder='views')

@application.route("/")
def hello_world():
    return "Hello, World of Flask on Docker! About" + \
           "<br /><small>"+time.strftime("%d/%h/%Y %H:%M:%S") + \
           "<br />@" + os.uname()[1] + \
           "<br />Hosted on: " + ' '.join(os.uname()) + \
           "</small>"

@application.route("/about")
def about():
    return render_template('about.html',  \
                            datetime=time.strftime("%d/%h/%Y %H:%M:%S"),  \
                            container=os.uname()[1],  \
                            hosted=' '.join(os.uname()))
