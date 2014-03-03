flask-peewee-example
====================

A tiny example of a flask-peewee powered webapp inspired by the official doc.

This example include two models : Author and Note (OneToMany). It provides an administration zone and a REST API.

Setup
-----
```bash
$ pip install flask-peewee
$ python run_project.py
```

The admin interface will be accessible at `http://localhost:8011/admin`. You can use this login/password : `serge / egres`.

More
----
* [peewee docs](http://peewee.readthedocs.org/)
* [flask-peewee docs](http://flask-peewee.readthedocs.org/)
