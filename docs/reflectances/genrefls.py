#!/usr/bin/env python

# This script will generate Markdown for the reflectances page
# using header.txt as a header.



from pcot import config,cameras
from os.path import basename
import os

config.loadReflectances()

with open("header.txt") as f:
    print(f.read())
    

for x in cameras.getReflectanceNames():
    c = cameras.getReflectance(x)

    patchlist = ", ".join(c.patches)

    sz = os.stat(c.path).st_size
    print (f"\n---\n\n### {x} ({c.typename})\n\n{c.metadata.description}")
    print (f"\nPatches: {patchlist}\n")
    fn = basename(c.path)
    print(f"\n[{fn}]({fn}) - {sz} bytes\n")

