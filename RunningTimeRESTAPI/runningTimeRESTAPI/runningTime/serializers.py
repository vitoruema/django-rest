from rest_framework import serializers
from . import Task, RunningTime


class TrainInfoSerializer(serializers.Serializer):
    train_type = serializers.CharField(required=True, max_length=100)
    train_length = serializers.IntegerField(required=True)
    segments = serializers.ListField(required=True,
                                     child=serializers.ListField(required=True,
                                                                 child=serializers.ListField(required=True,
                                                                                             child=serializers.CharField(required=True, max_length=100))))
    track_length = serializers.DictField(required=True,
                                         child=serializers.FloatField(required=True))
    pred_ini = serializers.FloatField(required=True)

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class RunningTimeSerializer(serializers.Serializer):
    running_time = serializers.DictField(required=True,
                                         child=serializers.FloatField(required=True))

    def create(self, validated_data):
        return RunningTime(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
