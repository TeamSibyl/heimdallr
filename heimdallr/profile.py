from pprint import PrettyPrinter


class Profile(object):
    """
    This class represents a profile of a segment. It shows all the things that
    the segment does.
    """
    def __init__(self, segment_id="unknown", entries={}):
        """
        segment_id is a string that identifies the segment
        entries is a dictionary, where keys are a type of syscall/library call,
        and values are specific details, which may or may not be dictionaries
        as well
        """
        self.segment_id = segment_id
        self.entries = entries

    def pprint(self):
        p = PrettyPrinter(indent=2)
        print("Profile for segment {}:".format(self.segment_id))
        for i in self.entries:
            p.pprint(i)
        print()
