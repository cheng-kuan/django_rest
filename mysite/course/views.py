from django.shortcuts import render
from .models import Course

from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CourseCollection(APIView):

    def post(self, request):
    	course_name = request.data.get('course_name', '')
    	course_desc = request.data.get('course_desc', '')
    	course = Course(user=request.user, course_name=course_name, course_desc=course_desc)
    	course.save()
    	return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        course_list = Course.objects.filter(user=request.user)
        res_data = list()
        for course in course_list:
            res_data.append(course.course_name+": "+course.course_desc)
        return Response(res_data, status=status.HTTP_200_OK)

    def put(self, request):
    	course_name = request.data.get('course_name', '')
    	course_desc = request.data.get('course_desc', '')
    	course = get_object_or_404(Course, user=request.user, course_name=course_name)
    	course.course_desc = course_desc
    	course.save()
    	return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        course_name = request.data.get('course_name', '')
        course = get_object_or_404(Course, user=request.user, course_name=course_name)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseDetail(APIView):

    def get(self, request, course_name):
        course = get_object_or_404(Course, user=request.user, course_name=course_name)
        res_data = model_to_dict(course, fields=['course_name', 'course_desc'])
        print(res_data)
        return Response(status=status.HTTP_200_OK)