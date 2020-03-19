from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from runningTime.serializers import TrainInfoSerializer, RunningTimeSerializer
from . import RunningTime
from .core.running_time_calculator import running_time


@api_view(['GET', 'POST'])
def get_running_time(request, format=None):
    if request.method == 'GET':
        serializer = TrainInfoSerializer(data=request.data)
        if serializer.is_valid():
            d = serializer.data

            x = RunningTime(running_time=running_time(d["train_type"], d["train_length"], d["segments"],
                                                      d["track_length"], d["segments"][0][0][0], d["pred_ini"]))
            resp = RunningTimeSerializer(x)

            return Response(resp.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)