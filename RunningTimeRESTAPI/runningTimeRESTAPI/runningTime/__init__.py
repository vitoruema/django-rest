class TrainInfo(object):
    def __init__(self, **kwargs):
        for field in ('train_type', 'train_length', 'segments', 'track_length', 'pred_ini'):
            setattr(self, field, kwargs.get(field, None))


class RunningTime(object):
    def __init__(self, **kwargs):
        setattr(self, 'running_time', kwargs.get('running_time', None))


class ErrorMessage(object):
    def __init__(self, **kwargs):
        setattr(self, 'message', kwargs.get('message', None))