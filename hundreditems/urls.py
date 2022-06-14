from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.hundred_items, name='hundred_items'),
]