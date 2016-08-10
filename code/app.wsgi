# -*- coding: UTF-8 -*-
'''
Application: flask
Modulue: application starting point
description: Tasting docker, redis, kafka
author: Adriano dos Santos Vieira <adriano.svieira at google.com>
character encoding: UTF-8
'''
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
reload(sys)
sys.setdefaultencoding('UTF-8')

from main import application
