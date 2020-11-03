from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Song
from .serializers import SongSerializer

class ApiView(APIView):
    def get(self, request, *args, **kwargs):
        songs = Song.objects.all()

        language = request.GET.get('language')
        if language != None:
            songs = Song.objects.filter(language=language)

        artist = request.GET.get('artist')
        if artist != None:
            songs = songs.filter(artist=artist)

        category = request.GET.get('category')
        if category != None:
            songs = songs.filter(category=category)

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        return Response({"error": "You have given the wrong request method"}, status=400)



def home(request):
    return render(request, 'index.html')