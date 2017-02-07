from django.conf.urls import url
from course import views

urlpatterns = [
    url(r'^$', views.CourseCollection.as_view()),
    url(r'^(?P<course_name>\w+)/$', views.CourseDetail.as_view()),
]