from django.shortcuts import render
from .models import Music
from django.http import HttpRequest,JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


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


@csrf_exempt
def music_url_list(request:HttpRequest):
    if request.method == "POST":
        music_url = request.POST.get("music_url")
        status = request.POST.get("status")
        print(music_url)
        print(status)

        current_music = Music.objects.get(music_file=music_url)
        if status == "next":
            print(True)
            next_music_id = current_music.id + 1
            music = Music.objects.get(id=next_music_id)
            
            music_data = {
                    "id": music.id,
                    "title": music.title,
                    "musician":music.musician,
                    "image": music.image.url,
                    "music_url": music.music_file.url,
                    }

        elif status == "previous":
            previous_music_id = current_music.id + 1
            try:
                music = Music.objects.get(id=previous_music_id)
            except Music.DoesNotExist:
                music = current_music


        return JsonResponse(music_data)
