import pickle
import numpy as np
from .exceptions.exceptions import *


def track_running_time(track, pred_ini, train_type, length, segment_origin):
    try:
        try:
            load_model = pickle.load(open("runningTime/core/models/{}.sav".format(track), "rb"))
            f = open("runningTime/core/tracknames.txt", "r")
        except FileNotFoundError:
            raise TrackNotFoundError

        var_dict = eval(f.read().replace('\n', ''))
        variaveis = var_dict[track]

        if train_type not in variaveis:
            raise TrainTypeNotFoundError
        elif segment_origin not in variaveis:
            raise SegmentOriginNotFoundError
        else:
            x = [1 if train_type == var or segment_origin == var else 0 for var in variaveis]
            x[0] = pred_ini
            x[1] = length

            print(segment_origin)
            print(x)

            return {track: load_model.predict(np.array(x).reshape(1, -1))[0]}
    except (TrackNotFoundError, TrainTypeNotFoundError):
        return {track: 0}


def running_time(train_type, length, segments, track_length, seg_ini_name, velo_ini):
    try:
        if not segments:
            return {}
        else:
            velo_media = 0
            running_time_dict = {}

            seg_head, *seg_tail = segments
            [seg_name], tracks = seg_head

            for track in tracks:
                try:
                    if velo_ini != 0:
                        running_time_dict = {**running_time_dict,
                                         **track_running_time(track, track_length[track] / velo_ini,
                                                      train_type, length, seg_ini_name)}
                except TypeError:
                    pass
                if running_time_dict[track] != 0:
                    velo_media += track_length[track] / running_time_dict[track]

            velo_media = velo_media / len(tracks)

            return {**running_time_dict,
                    **running_time(train_type, length, seg_tail, track_length, seg_name, velo_media)}
    except KeyError:
        raise TrackLengthNotFoundError

