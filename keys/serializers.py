from rest_framework import serializers
from register.models import Card


class MasterKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'lock')
