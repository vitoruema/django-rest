from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers


class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.RegrEntrySerializer

    def retrive(self, request):
        serializer = serializers.RegrEntrySerializer(data=request.data)
        if serializer.is_valid():
            regrEntry = serializer.save()
            print(regrEntry)
