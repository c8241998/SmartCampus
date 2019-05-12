from django.shortcuts import render
from util.json import jsonRes
from apps.course import models
# Create your views here.

def create(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        course_school = request.POST.get('course_school')
        course_teacher = request.POST.get('course_school')
        course_classroom = request.POST.get('course_classroom')
        course_students = request.POST.get('course_students')

        exist = models.Course.objects.filter(course_id=course_id).exists()
        if not exist:
            course = models.Course()
            course.course_id = course_id
            course.course_name = course_name
            course.course_school = course_school
            course.course_teacher = course_teacher
            course.course_classroom = course_classroom
            course.course_students = course_students
            course.save()
            return jsonRes('success',200,{})
        else:
            return jsonRes('id_conflict',400,{})


def course(request,id):
    if request.method == 'POST':
        exist = models.Course.objects.filter(course_id=id).exists()
        if not exist:
            return jsonRes('id_not_found',404,{})
        else:
            course_name = request.POST.get('course_name')
            course_school = request.POST.get('course_school')
            course_teacher = request.POST.get('course_school')
            course_classroom = request.POST.get('course_classroom')
            course_students = request.POST.get('course_students')

            course = models.Course.objects.get(course_id=id)
            course.course_name = course_name
            course.course_school = course_school
            course.course_teacher = course_teacher
            course.course_classroom = course_classroom
            course.course_students = course_students
            course.save()
            return jsonRes('success', 200, {})


    if request.method == 'GET':
        exist = models.Course.objects.filter(course_id=id).exists()
        if not exist:
            return jsonRes('id_not_found', 404, {})
        else:
            course = models.Course.objects.get(course_id=id)
            return jsonRes('success', 200, course)

    if request.method == 'DELETE':
        exist = models.Course.objects.filter(course_id=id).exists()
        if not exist:
            return jsonRes('id_not_found', 404, {})
        else:
            models.Course.objects.get(course_id=id).delete()
            return jsonRes('success', 200, {})