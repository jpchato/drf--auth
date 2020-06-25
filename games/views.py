from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Game
from .serializers import GameSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class GamesList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GamesDetail(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthorOrReadOnly,)