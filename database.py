#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_peewee.db import Database
from app import app

db = Database(app)
