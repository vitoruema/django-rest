from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, RunningTimeSerializer
from . import RunningTime

import pickle
import numpy as np


def track_running_time(track, pred_ini, train_type, length, segment_origin):
    f = open("snippets/tracknames.txt", "r")
    var_dict = eval(f.read().replace('\n', ''))
    variaveis = var_dict[track]
    x = [1 if train_type == var or segment_origin == var else 0 for var in variaveis]
    x[0] = pred_ini
    x[1] = length

    load_model = pickle.load(open("snippets/models/{}.sav".format(track), "rb"))
    #print(load_model.predict(np.array(x).reshape(1, -1)))

    return {track: load_model.predict(np.array(x).reshape(1, -1))[0]}


def running_time(train_type, length, segments, track_length, seg_ini_name, pred_ini):
    pred_media = 0
    running_time_dict = {}
    if not segments:
        return {}
    else:
        seg_head, *seg_tail = segments
        seg_name, tracks = seg_head
        for track in tracks:
            running_time_dict = track_running_time(track, pred_ini, train_type, length, seg_ini_name)
            pred_media += running_time_dict[track]

        pred_media = pred_media / len(tracks)

        return {**running_time_dict, **running_time(train_type, length, seg_tail, track_length, seg_name, pred_media)}


# track_running_time("CL10.81508", 20, "TRAIN_TYPE_ID_BOre", 2360, "SEGMENT_ORIGIN_CL52BT")

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer = SnippetSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            d = serializer.data
            print(running_time(d["train_type"], d["train_length"], d["segments"],
                               d["track_length"], d["segments"][0][0][0], d["pred_ini"]))

            x = RunningTime(running_time=running_time(d["train_type"], d["train_length"], d["segments"],
                                                      d["track_length"], d["segments"][0][0][0], d["pred_ini"]))
            resp = RunningTimeSerializer(x)
            print(x)

            return Response(resp.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)

    elif request.method == 'POST':
        print("ok")
        serializer = SnippetSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
