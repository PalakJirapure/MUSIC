from django.shortcuts import render
from Groovy.models import Song

def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song': song})

def songs(request):
    song = Song.objects.all
    return render(request, 'Groovy/songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'Groovy/songpost.html', {'song': song})

def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request, 'Groovy/search.html', {"songs": qs})