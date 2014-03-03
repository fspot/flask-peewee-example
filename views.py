#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
from models import Author, Note

@app.route('/')
def index():
    return u'<h1>Hello !</h1><a href="notes/">See all notes ←</a>'

@app.route('/notes/')
def list_notes():
	notes = Note.select().order_by(Note.created.desc()).limit(100)
	notes = u'\n'.join(unicode(n) for n in notes)
	return u'<h1>Notes</h1><pre>%s</pre>' % notes
