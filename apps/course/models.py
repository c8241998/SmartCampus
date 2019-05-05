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

    def get_course(self, course_id):
        course = Course.objects.get(course_id=course_id)
        return course


    def delete_course(self, course_id):
        Course.objects.filter(course_id=course_id).delete()
        return 'success'


    def update_sourse(self, course_id, course_name, course_school, course_teacher, course_classroom):
        course = Course.objects.get(course_id=course_id)
        course.course_name=course_name
        course.course_school=course_school
        course.course_teacher=course_teacher
        course.course_classroom=course_classroom
        course.save()


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
