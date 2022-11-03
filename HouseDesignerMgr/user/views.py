from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    users = get_user_model()

    return HttpResponse(users.objects.all())