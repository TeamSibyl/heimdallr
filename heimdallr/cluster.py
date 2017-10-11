from argwrapper import ArgWrapper
from segmentationengine import SegmentationEngine
from profilerengine import ProfilerEngine


class Cluster(object):
    """
    Driver class for the Heimdall project. Maintains a local angr Project to
    direct actual analysis to. Will probably be restructured later, to allow
    it to talk to multiple segmenters and profilers in parallel over network
    communication(probably through celery).
    """

    def __init__(self, binary, **kwargs):
        self.angr_args = (binary, kwargs)

    def get_segments(self):
        s = SegmentationEngine(self.angr_args)
        return s.get_segments()

    def profile(self, segment):
        """
        Perform analysis on the segment, return a profile showing the
        possibilities for what role that segment has
        """
        p = ProfilerEngine(self.angr_args)
        return p.profile(segment)
