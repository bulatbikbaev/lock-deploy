from rest_framework import generics, status
from .models import Lock, Card, Key
from .serializers import LockSerializer, CardSerializer, KeySerializer
from rest_framework.response import Response


# TODO: Add permissions and logs


class LockList(generics.ListCreateAPIView):
    serializer_class = LockSerializer
    queryset = Lock.objects.all()


class CardList(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class KeyList(generics.ListCreateAPIView):
    serializer_class = KeySerializer

    def get_queryset(self):
        """
        Return new key with generated code
        """
        queryset = Key.objects.all()
        key_id = self.request.query_params.get('id', None)
        queryset = queryset.filter(id=key_id)
        return queryset


