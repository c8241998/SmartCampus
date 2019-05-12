from django.db import models
from apps.student.models import *
# Create your models here.


class Course(models.Model):
    course_id = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        primary_key=True
    )

    course_name = models.CharField(
        max_length=10
    )
    course_school = models.CharField(max_length=20)
    course_teacher = models.CharField(max_length=20)
    course_classroom = models.CharField(max_length=20)
    course_students = models.CharField(max_length=1000)

    def __str__(self):
        dir = {}
        dir['course_name'] = self.course_name
        dir['course_id'] = self.course_id
        return dir


class Course_student(models.Model):
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE
    )


    def get_course_student(self, course_id):
        result = Course_student.objects.filter(course_id__course_id=course_id)
        return result
