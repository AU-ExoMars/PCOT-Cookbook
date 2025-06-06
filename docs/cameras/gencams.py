#!/usr/bin/env python

# This script will generate Markdown for the cameras page,
# using header.txt as a header.



from pcot import config,cameras
from os.path import basename
import os

config.loadCameras()

with open("header.txt") as f:
    print(f.read())

for x in cameras.getCameraNames():
    c = cameras.getCamera(x)
    p = cameras.getCamera(x).params.params
    
    if "OLD" not in p.name and p.name != "TEST":
        sz = os.stat(c.fileName).st_size
        print (f"\n---\n\n### {p.name}\n\n{p.description}")
        fn = basename(c.fileName)
        
        if p.has_flats:
            print("* Has flatfield data")
        if p.has_reflectances:
            print("* Has reflectance data for: "+", ".join(c.params.reflectances.keys()))

        print(f"\n[{fn}]({fn}) - {sz} bytes\n")
