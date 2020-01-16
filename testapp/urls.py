from django.urls import re_path
from django_morepath.views import make_morepath_view
from .app import app


urlpatterns = [re_path("(.*)", make_morepath_view(app))]

