from django.shortcuts import render
from apps.student import models
from util.json import jsonRes
import base64
from django.http import HttpResponse
# Create your views here.


def create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        student_school = request.POST.get('student_school')
        student_avatar = request.POST.get('student_avatar')
        student_email = request.POST.get('student_email')
        student_class = request.POST.get('student_class')
        try:
            temp = models.Student.objects.get(student_id=student_id)
            return jsonRes("id_conflict", 400, {})
        except models.Student.DoesNotExist:
            student = models.Student()
            student.student_id = student_id
            student.student_name = student_name
            student.student_school = student_school
            student.student_avatar = student_avatar
            student.student_email = student_email
            student.student_class = student_class
            student.save()
            return jsonRes("success", 200, {})


def student(request,id):
    if request.method == 'POST':
        exist = models.Student.objects.filter(student_id=id).exists()
        if not exist:
            return jsonRes('id_not_found',404,{})
        else:
            student_name = request.POST.get('student_name')
            student_school = request.POST.get('student_school')
            student_avatar = request.POST.get('student_avatar')
            student_email = request.POST.get('student_email')
            student_class = request.POST.get('student_class')
            student = models.Student.objects.get(student_id=id)
            student.student_name = student_name
            student.student_school = student_school
            student.student_avatar = student_avatar
            if student_email:
                student.student_email = student_email
            if student_class:
                student.student_class = student_class
            student.save()
            return jsonRes("success", 200, {})

    if request.method == 'GET':
        exist = models.Student.objects.filter(student_id=id).exists()
        if not exist:
            return jsonRes('id_not_found', 404, {})
        else:
            student = models.Student.objects.get(student_id=id)
            return jsonRes('success', 200, str(student))

    if request.method == 'DELETE':
        exist = models.Student.objects.filter(student_id=id).exists()
        if not exist:
            return jsonRes('id_not_found', 404, {})
        else:
            models.Student.objects.get(student_id=id).delete()
            return jsonRes('success', 200, {})


def student_avatar(request, id):
    exist = models.Student.objects.filter(student_id=id).exists()
    if not exist:
        return jsonRes('id_not_found', 404, {})
    else:
        student = models.Student.objects.get(student_id=id)
        avatar = student.student_avatar
        img = base64.b64decode(avatar)
        return HttpResponse(img, content_type="image/png")


