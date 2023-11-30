from django.shortcuts import render
from .models import Music
from django.http import HttpRequest


def music(request:HttpRequest):
    musics = Music.objects.all()

    context = {
            "musics":musics,
            }
    return render(request,"music.html",context)



def listen(request:HttpRequest,music_id:int):
    music = Music.objects.get(id=music_id)

    context = {
            "music":music,
            }
    return render(request,"listen.html",context)

