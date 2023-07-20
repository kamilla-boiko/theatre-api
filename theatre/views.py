from rest_framework import viewsets

from theatre.models import Play
from theatre.serializers import PlaySerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
