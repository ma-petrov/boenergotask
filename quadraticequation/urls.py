from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.quadratic_equation, name='quadratic_equation'),
    re_path(r'^solution/$', views.solution, name='solution'),
]