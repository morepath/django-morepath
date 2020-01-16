===============
django-morepath
===============

Introduction
============

**NOTE: This is a pre-alpha version of Django-morepath. A few tests work, but
more work is to be done. I'm looking for help with further integration!**

Django-morepath is a framework for Django_ to build REST APIs with Django. It
does this by integrating the powerful but lightweight Morepath_ framework. You
can see django-morepath as an alternative to Django REST framework that is less
complex yet in some ways more flexible. My hope is that developers will like
how Morepath-style REST applications are organized.

Morepath has existed as an independent Python web framework for some years. It
provides a different way to create and organize REST APIs. Django is
a very popular Python web framework. I was looking for a way to leverage
the strengths of Morepath within the existing Django platform.

Django's platform features an ORM with a powerful database migration system.
Morepath can easily integrate with this ORM so it can publish Django model
instances.

Isn't integrating another web framework into Django overkill?
=============================================================

You'd think so, but django-morepath is in fact surprisingly lightweight - the
core library and its few core dependencies (reg and dectate) amount to about
half the size in lines of code in Django REST Framework!

This isn't a fair comparison, as Django REST Framework also implements a
serializer library where Morepath does not, but even if you throw in a
serializer library like Marshmallow_ the combination is still smaller
than Django REST Framework. Morepath has integration with Marshmallow in
more.marshmallow_.

.. _more.marshmallow: https://github.com/morepath/more.marshmallow

How to use it?
--------------

Morepath lets you construct application instances that lets you expose objects
(such as Django model instances) to paths (URLs). You can then provide one or
more views for those paths. Django-morepath lets you expose a Django
application on a Django URL.

Here is a simple example. First, we define this in `models.py`:

.. code:: python

  from django.db import models


  class Person(models.Model):
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)


As you can see, this is a normal Django model -- nothing special. Any
Django model will work.

Now we are going to create a `GET` request so that a path like `/persons/1`
gives back some JSON. You can put this code in any module that gets imported --
I've chosen here to put it in `app.py`:

.. code:: python

  import morepath
  from .models import Person

  class App(morepath.App):
      pass

  @App.path(model=Person, path="/persons/{id}")
  def get_person(id=0):
      return Person.objects.filter(pk=id).first()

  @App.json(model=Person)
  def person_get(self, request):
      return {"first_name": self.first_name, "last_name": self.last_name}

  app = App()

Putting it all in `app.py` works but isn't recommended for a larger
codebase - you can separate a package into an `app.py`, `paths.py` and
`views.py` for instance.

Finally we need to mount the Morepath `app` instance in a Django URL in
`urlpatterns.py`:

.. code:: python

  from django.urls import re_path
  from django_morepath import make_morepath_view
  from .app import app

  urlpatterns = [re_path("(.*)", make_morepath_view(app))]

And that's it! The `Morepath documentation`_ contains a lot more
information:

.. _`Morepath documentation`: https://morepath.readthedocs.io

.. _Django: https://www.djangoproject.com/

.. _Morepath: https://morepath.readthedocs.io/

