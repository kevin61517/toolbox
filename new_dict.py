class Dict(dict):
    def __init__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, dict):
                raise ValueError('Not type dict')
            for key, value in arg.items():
                self[key] = value
        for k, v in kwargs.items():
            self[k] = v

    def set(self, *args):
        for arg in args:
            for k, v in arg.items():
                self[k] = v

