from django.shortcuts import render
from .models import Music

def music_list(request):
    music_list = Music.objects.all()
    context = {
        'musics' : music_list
    }
    return render (request,"music/music.html",context)
