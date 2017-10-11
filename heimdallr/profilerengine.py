from angr import Project
from profile import Profile

class ProfilerEngine(object):
    """
    A basic class that, given details about a segment, produces a profile
    for it. It's main interface is the profile(segment) method
    """
    def __init__(self,angr_args):
        self.b = angr.Project(*angr_args.get_args(),**angr_args.get_kwargs())

    def profile(self, segment):
    """
    The main interface to this class. Given a segment desciption, produce a
    profile descibing its functioning. Pure function.
    """
    # TODO fill this out
    pass
