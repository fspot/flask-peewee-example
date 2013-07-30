import datetime
from peewee import *
from database import db
from flask_peewee.admin import ModelAdmin

class Author(db.Model):
    name = TextField()
    age = IntegerField()

    def __unicode__(self):
        return '%s' % (self.name)

class AuthorAdmin(ModelAdmin):
    columns = ('name', 'age',)


class Note(db.Model):
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)
    author = ForeignKeyField(Author, related_name='notes')

class NoteAdmin(ModelAdmin):
    columns = ('message', 'author', 'created',)
    foreign_key_lookups = {'author': 'name'}

