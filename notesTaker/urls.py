from django.conf.urls import url
from . import views

app_name="noteTaker"

# connect urls with functions within views.py
urlpatterns = [
    url(r'^/$', views.login, name='login'),
]
