# mysite/users/urls.py

from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.UserCreate.as_view()),
    url(r'^login/$', views.UserLogin.as_view()),
    url(r'^logout/$', views.UserLogout.as_view()),
]


