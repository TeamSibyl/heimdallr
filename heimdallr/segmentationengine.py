import angr


class SegmentationEngine(object):
    def __init__(self, angr_args):
        b = angr.Project(angr_args[0], load_options={'auto_load_libs': False}, **angr_args[1])
        self.func_manager = b.analyses.CFGAccurate().kb.functions

    def get_segments(self):
        """
        Returns an iterable representing a single segment. Right now, a
        segment is single function.
        """
        # TODO implement this to return an iterable of type Segment
        return [1,2]
