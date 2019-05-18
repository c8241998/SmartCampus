# Generated by Django 2.2.1 on 2019-05-18 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=10)),
                ('course_school', models.CharField(max_length=20)),
                ('course_teacher', models.CharField(max_length=20)),
                ('course_classroom', models.CharField(max_length=20)),
                ('course_students', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Course_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]