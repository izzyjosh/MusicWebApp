from django.shortcuts import render
from .models import Music
from django.http import HttpRequest


def music(request:HttpRequest):
    musics = Music.objects.all()

    context = {
            "musics":musics,
            }
    return render(request,"music.html",context)
