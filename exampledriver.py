from heimdallr import Cluster
from heimdallr.profile import Profile
"""
This file shows an example of a program utilizing Heimdall
"""

p = Cluster("/usr/bin/true")

for segment in p.get_segments():
    prof = p.profile(segment)
    prof.pprint()
