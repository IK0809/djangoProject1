from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("ようこそ")


def index2(request):
    return HttpResponse('ようこそ２')
