#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
from database import db
from models import Note, Author
from admin import setup_admin
from rest import setup_api

# Auth and Admin stuff
auth, admin = setup_admin()
api = setup_api(auth)

def setup_tables():
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Author.create_table(fail_silently=True)

if __name__ == '__main__':
    setup_tables()
    import views
    import feed
    app.run(host="0.0.0.0", port=8011)
