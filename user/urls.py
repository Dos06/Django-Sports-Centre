from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'', views.test),
    # /user/
    url(r'^$',  views.index, name='index'),     # ^$ means empty space
    # /user/*member_id*
    url(r'^(?P<member_id>[0-9]+)/$', views.detail, name='detail'),
]