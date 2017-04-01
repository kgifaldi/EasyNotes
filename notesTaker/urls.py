from django.conf.urls import url
from . import views

app_name="noteTaker"

# connect urls with functions within views.py
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^add_class/$', views.add_class, name='add_class'),
    url(r'^add_notes/$', views.add_notes, name='add_notes'),
    url(r'^view_classes/$', views.view_classes, name='view_classes')
]
