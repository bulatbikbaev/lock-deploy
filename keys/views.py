from rest_framework import generics
from .serializers import MasterKeySerializer
from register.models import Card


# TODO: Add permissions


class MasterKeyList(generics.ListAPIView):
    queryset = Card.objects.filter(is_master=True)
    serializer_class = MasterKeySerializer


class MasterKeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.filter(is_master=True)
    serializer_class = MasterKeySerializer
