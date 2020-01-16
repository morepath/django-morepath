django-morepath
===============

NOTE: This is a pre-alpha version of Django-morepath. I'm looking for help
with further integration!

Django-morepath is a framework for Django_ to build REST APIs with Django. It
does this by integrating the powerful but lightweight Morepath_ framework. You
can see django-morepath as an alternative to Django REST framework that is less
complex yet in some ways more flexible. I think developers will like in how
Morepath-style REST applications are organized.

Morepath has existed as an independent Python web framework for some years. It
provides a different way to create and organize REST APIs. Django is
a very popular Python web framework. I was looking for a way to leverage
the strengths of Morepath within the existing Django platform.

Django's platform features an ORM with a powerful database migration system.
Morepath can easily integrate with this ORM so it can publish Django model
instances.

.. _Django: https://www.djangoproject.com/

.. _Morepath: https://morepath.readthedocs.io/

