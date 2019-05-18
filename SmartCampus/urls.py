"""SmartCampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.account import views as accountview
from apps.student import views as student
from django.conf.urls import url
from apps.course import views as course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', accountview.login),
    path('register', accountview.register),
    path('student/create', student.create),
    path('course/create', course.create),
    url(r'^student/(?P<id>\w+)/$', student.student,name="student"),
    url(r'^student/(?P<id>\w+)/avatar$', student.student_avatar, name="student_avatar"),
    url(r'^course/(?P<id>\w+)/$', course.course, name="course"),
    url(r'^course/(?P<id>\w+)/checkin$', course.checkin, name='coursechecnin')
]
