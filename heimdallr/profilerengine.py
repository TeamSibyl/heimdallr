from angr import Project
from profile import Profile
from itertools import chain

class ProfilerEngine(object):
    """
    A basic class that, given details about a segment, produces a profile
    for it. This class is the most complex part of this project
    """
    def __init__(self, angr_args):
        self.b = Project(angr_args[0], **angr_args[1])

    def profile(self, segment):
        """
        The main interface to this class. Given a segment desciption, produce a
        profile descibing its functioning. Pure function.
        """
	a = [block.vex.operations for block in segment.blocks]
	a = list(chain(*a))
	d = {}	
	for op in a:
		if op in d:
			d[i]+=1
		else:
			d[i] = 1
	return Profile(segment.name, d)
