
class ArgWrapper(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_args(self):
        return self.args

    deg get_kwargs(self):
        return self.kwargs
