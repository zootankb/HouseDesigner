from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    return HttpResponse('AssetBundle包')