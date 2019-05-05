from django.db import models

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


    def __str__(self):
        dir = {}
        dir['student_name'] = self.student_name
        dir['student_id'] = self.student_id
        return dir