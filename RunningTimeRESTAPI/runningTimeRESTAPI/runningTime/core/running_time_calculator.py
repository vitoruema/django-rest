import pickle
import numpy as np


def track_running_time(track, pred_ini, train_type, length, segment_origin):
    f = open("runningTime/core/tracknames.txt", "r")
    var_dict = eval(f.read().replace('\n', ''))
    variaveis = var_dict[track]
    x = [1 if train_type == var or segment_origin == var else 0 for var in variaveis]
    x[0] = pred_ini
    x[1] = length

    load_model = pickle.load(open("runningTime/core/models/{}.sav".format(track), "rb"))
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