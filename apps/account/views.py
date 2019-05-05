from datetime import time
from django.contrib import auth
from django.core.serializers import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.account import models
from util.json import jsonRes

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            re = models.MyUser.objects.get(email=email)
        except models.MyUser.DoesNotExist:
            return jsonRes("user_not_found",400,{})
        re = auth.authenticate(request, username=email, password=password)
        if re is None:
            return jsonRes("password_incorrect", 401, {})
        auth.login(request, re)

        return jsonRes("success", 200, {})


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        try:
            re = models.MyUser.objects.get(email=email)
            return jsonRes("email_conflict", 400, {})
        except models.MyUser.DoesNotExist:
            try:
                re = models.MyUser.objects.get(username=username)
                return jsonRes("user_conflict", 400, {})
            except models.MyUser.DoesNotExist:
                user = models.MyUser()
                user.email = email
                user.set_password(password)
                user.username = username
                user.save()
                return jsonRes("success", 200, {})

@login_required
def logout(request):
    auth.logout(request)