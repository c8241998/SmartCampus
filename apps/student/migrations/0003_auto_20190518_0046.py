# Generated by Django 2.2.1 on 2019-05-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190518_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_avatar',
            field=models.ImageField(upload_to=''),
        ),
    ]
