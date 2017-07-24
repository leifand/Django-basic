from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^clear', views.clear_session_keys),
    url(r'^process_money', views.process_money)
]
