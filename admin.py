from flask_peewee.admin import Admin
from flask_peewee.auth import Auth

from app import app
from database import db
from models import Note, NoteAdmin, Author, AuthorAdmin

def setup_admin():
    auth = Auth(app, db)
    admin = Admin(app, auth)
    admin.register(Note, NoteAdmin)
    admin.register(Author, AuthorAdmin)
    auth.register_admin(admin)
    admin.setup()
    return auth, admin

