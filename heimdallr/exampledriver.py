from project import Project
from profile import Profile
"""
This file shows an example of a program utilizing Heimdall
"""

p = Project("/user/bin/true")

for segment in p.get_segments():
    prof = p.profile(segment)
    prof.pprint()
