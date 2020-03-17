from sklearn import linear_model
import pandas
import pickle
import numpy as np

def running_time(train_type, , length, percurso, pred_ini, nul):
    if percurso is not None:
        print(track_running_time(track, pred_ini, )train_type, )




def track_running_time(track, pred_ini, train_type, length, segment_origin):
    f = open("src/tracknames.txt", "r")
    var_dict = eval(f.read().replace('\n', ''))
    variaveis = var_dict[track]
    x = [1 if train_type == var or segment_origin == var else 0 for var in variaveis]
    x[0] = pred_ini
    x[1] = length
    print(x)

    load_model = pickle.load(open("src/models/{}.sav".format(track), "rb"))
    print(load_model.predict(np.array(x).reshape(1, -1)))


track_running_time("CL10.81508", 20, "TRAIN_TYPE_ID_BOre", 2360, "SEGMENT_ORIGIN_CL52BT")
