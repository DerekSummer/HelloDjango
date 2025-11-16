from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello! You're at the index.")

def mycmdb(request):
    return HttpResponse("Hello! You're at the mycmdb page.")

