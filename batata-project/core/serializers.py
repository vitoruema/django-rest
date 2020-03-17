from django.forms import widgets
from rest_framework import serializers
from core.models import RegrEntry


class RegrEntrySerializer(serializers.Serializer):
    type = serializers.CharField()
    length = serializers.FloatField()
    ini_velo = serializers.FloatField()
    route = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField()))

    def create(self, validated_data):
        return RegrEntry()

    # talvez desnecessario
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
