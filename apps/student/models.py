from django.db import models
import json
# Create your models here.


class Student(models.Model):
    student_id = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        primary_key=True
    )

    student_name = models.CharField(
        max_length=10
    )
    student_school = models.CharField(max_length=20)
    student_avatar = models.ImageField()
    student_email = models.EmailField(
        verbose_name='email address',
        max_length=40,
        unique=True,
    )
    student_class = models.CharField(max_length=20)


    def change_student(self, student_id, student_name, student_school, student_avatar, student_email, student_class ):
        student = Student.objects.get(student_id=student_id)
        student.student_name = student_name
        student.student_school = student_school
        student.student_avatar = student_avatar
        student.student_email = student_email
        student.student_class = student_class
        student.save()


    def get_student_by_id(self, student_id):
        student = Student.objects.get(studeng_id=student_id)
        return student


    def delete_by_id(self, student_id):
        Student.objects.filter(student_id=student_id).delete()
        return 'success'


    def __str__(self):
        dir = {}
        dir['student_name'] = self.student_name
        dir['student_id'] = self.student_id
        dir['student_school'] = self.student_school
        dir['school_email'] = self.student_email
        dir['school_class'] = self.student_class
        return json.dumps(dir)