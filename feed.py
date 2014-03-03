#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
from models import Note

from urlparse import urljoin
from flask import request
from werkzeug.contrib.atom import AtomFeed

def make_external(url):
    return urljoin(request.url_root, url)

@app.route('/notes.atom')
def notes_feed():
    """ Based on http://flask.pocoo.org/snippets/10/ """
    feed = AtomFeed('Notes feed', feed_url=request.url, url=request.url_root)
    notes = Note.select().order_by(Note.created.desc()).limit(100)
    for note in notes:
        feed.add(note.message[:40], unicode(note.message),
                 content_type='html',
                 author=note.author.name,
                 url=make_external('#'),
                 updated=note.created,
                 published=note.created)
    return feed.get_response()
