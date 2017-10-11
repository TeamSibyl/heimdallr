import angr


class SegmentationEngine(object):
    def __init__(self, angr_args):
        b = angr.Project(*angr_args.get_args,
                         load_options={'auto-load-libs': False},
                         **angr_args.get_kwargs)
        self.func_manager = b.analyses.CFGAccurate().kb.functions()

    def get_segments(self):
        """
        Returns an iterable representing a single segment. Right now, a
        segment is single function.
        """
        # TODO implement this to return an iterable of type Segment
        pass
