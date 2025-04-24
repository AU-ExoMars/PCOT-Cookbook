# Camera data

This directory contains camera definition files. These contain:

* what filters a camera has, and for each filter:
    * a name, position and description
    * centre wavelength, bandwidth etc.
* optional reflectance data for each filter for each patch in a target
* optional flat and dark fields (which make the file huge, but it can't
be helped)

Each file is a PCOT archive (``.parc`) file which should be placed
in the cameras directory. This must be specified in the `.pcot.ini` file
in the locations section:

```ini
[Locations]
...
cameras = /home/white/PCOT/cameras
```
If not specified, no cameras will be loaded! The `.pcot.ini` can be
found in the user's home directory.

## Camera files



---

### AUPE_LEFT

The Aberystwyth University PanCam Emulator, left WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats (when present) dated 2023-07-20, 40 images from each filter.

[aupeL.parc](cameras/aupeL.parc) - 72679418 bytes


---

### AUPE_LEFT_NOCALIB

The Aberystwyth University PanCam Emulator, left WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats (when present) dated 2023-07-20, 40 images from each filter.

[aupeL_nocalib.parc](cameras/aupeL_nocalib.parc) - 1829 bytes


---

### AUPE_RIGHT

The Aberystwyth University PanCam Emulator, right WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats dated 2023-07-20, 40 images from each filter.

[aupeR.parc](cameras/aupeR.parc) - 71504762 bytes


---

### AUPE_RIGHT_NOCALIB

The Aberystwyth University PanCam Emulator, right WAC only.
This dataset represents AUPE as it was on 4th March 2025.
Flats dated 2023-07-20, 40 images from each filter.

[aupeR_nocalib.parc](cameras/aupeR_nocalib.parc) - 1772 bytes


---

### PANCAM

The flight PanCam WAC instruments as they were on 4th March 2025.
This is a minimal data set with filters only.

[pancam.parc](cameras/pancam.parc) - 984 bytes


---

### TRAINING_GEOLOGY

The training PanCam instrument as it was on 4th March 2025.
This is the GEOLOGY set for the WAC.

[training1_geol.parc](cameras/training1_geol.parc) - 43068317 bytes


---

### TRAINING_RGB

The training PanCam instrument as it was on 4th March 2025.
This is the RGB/Solar set for the WAC.
This is a minimal data set with filters only.

[training2_rgb.parc](cameras/training2_rgb.parc) - 829 bytes

