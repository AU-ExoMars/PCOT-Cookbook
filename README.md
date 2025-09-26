# PCOT-Cookbook
Documented examples of common operations in PCOT

This is an mkdocs document, and for now it is hosted at
[cookbook.pale.org](cookbook.pale.org).


## How to create the build environment and build the site

Run these commands to create a conda environment and install
the necessary files:
```
conda create -n mkdocs python=3.9
conda activate mkdocs
pip install mkdocs-material
pip install mkdocs-mermaid2-plugin
```

Run them as individual commands, not in a script.

You can then use `mkdocs build` to build the site,
which will appear in the `site` directory. This can then be uploaded
to the server.

You can also run `mkdocs serve` to run a local web server for testing.

NOTE THAT `PYTHONPATH` needs to include "." so that it can find
extensions like `lightbox.py`

## Document structure

The recipes themselves are in `docs/recipes` and should be indexed in
`index.md`. The files are all in Markdown. Each graph should have
a graph file and at least one screenshot - these should be kept in
the `graphs` and `screenshots` directories under `docs/recipes`. Looking
at how existing recipes are structured will help enormously!


## Internal

### How to copy to sitehost via Windows

Build the files using `build`, copy them over to a Windows box (if you're
not building on one). Then mount sitehost on Windows:
```
\\sitehost.disk.aber.ac.uk\pcot-aber-ac-uk
```
and copy the files over.


### Mounting from Linux (deprecated)

How to mount on Linux; doesn't currently work:

```
sudo mount -t cifs -o rw,username=PAU\\jcf12,uid=jcf12 //sitehost.disk.aber.ac.uk/pcot-aber-ac-uk mountpoint
```

