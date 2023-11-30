from django.shortcuts import render
from .models import Music
from django.http import HttpRequest
from django.db.models import Q


def music(request:HttpRequest):
    if request.method == "POST":
        search = request.POST.get("search")
        musics = Music.objects.filter(
                title__icontains=search)
    else:
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

