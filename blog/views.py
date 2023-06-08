from django.shortcuts import render
from django.http import HttpResponse
import json# Create your views here.
import os
def home(request):
    return render(request, 'blog/index.html' , context={"name":"Otabek"})



os.chdir(os.getcwd() + "/blog")
def music(request):
    with open('tracks.json', 'r') as f:
        data = json.load(f)
    context = {
        'music': data,

        }
    return render(request, 'blog/music.html', context=context)
