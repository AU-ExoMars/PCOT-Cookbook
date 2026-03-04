# Camera data

<!-- Note to authors: Do not edit the index.md directly, edit 
     header.txt and use ./gencams.py. See the README. -->

This directory contains camera definition files. These contain:

* what filters a camera has, and for each filter:
    * a name, position and description;
    * centre wavelength, bandwidth etc.;
    * ideally a set of response data, which is either a single
      value for each wavelength or a set of values over a range
      of transmission angles. If not present, the response will
      be simulated as a gaussian based on the other parameters.

* optional flat and dark fields (which make the file huge, but it can't
be helped)

Each file is a PCOT archive (`.parc`) file which should be placed
in the cameras directory. This must be specified in the `.pcot.ini` file
in the locations section:

```ini
[Locations]
cameras = /home/white/PCOT/cameras
```
If not specified, no cameras will be loaded! The `.pcot.ini` can be
found in the user's home directory.

## Camera files

!!! danger
    At this stage of development the data may be inaccurate!




---

### AUPE_LEFT

The Aberystwyth University PanCam Emulator, left WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats (when present) dated 2023-07-20, 40 images from each filter.

* Has flatfield data

[aupeL.parc](aupeL.parc) - 72679036 bytes


---

### AUPE_LEFT_NOCALIB

The Aberystwyth University PanCam Emulator, left WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats (when present) dated 2023-07-20, 40 images from each filter.


[aupeL_nocalib.parc](aupeL_nocalib.parc) - 1436 bytes


---

### AUPE_LEFT_OFFSET_NOCALIB

The Aberystwyth University PanCam Emulator, left WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats (when present) dated 2023-07-20, 40 images from each filter.
THIS FILE HAS THE FILTERS OFFSET BY ONE TO COMPENSATE FOR AN ERROR.
USE ONLY FOR IMAGES CAPTURED BY VELOCIRAPDER PRIOR TO JUNE 2025


[aupeL_offset_nocalib.parc](aupeL_offset_nocalib.parc) - 1668 bytes


---

### AUPE_RIGHT

The Aberystwyth University PanCam Emulator, right WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats, when present, dated 2023-07-20, 40 images from each filter.

* Has flatfield data

[aupeR.parc](aupeR.parc) - 71504408 bytes


---

### AUPE_RIGHT_NOCALIB

The Aberystwyth University PanCam Emulator, right WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats, when present, dated 2023-07-20, 40 images from each filter.


[aupeR_nocalib.parc](aupeR_nocalib.parc) - 1448 bytes


---

### PANCAM

The flight PanCam WAC instruments as they were on 4th March 2025.
This is a minimal data set with filters only.


[pancam.parc](pancam.parc) - 1518 bytes


---

### TRAINING_GEOLOGY

The training PanCam instrument as it was on 4th March 2025.
This is the GEOLOGY set for the WAC. 

* Has flatfield data

[training1_geol.parc](training1_geol.parc) - 43121778 bytes


---

### TRAINING_RGB

The training PanCam instrument as it was on 4th March 2025.
This is the RGB/Solar set for the WAC.
This is a minimal data set with filters only.


[training2_rgb.parc](training2_rgb.parc) - 1347 bytes

