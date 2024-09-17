import numpy as np
from pathlib import Path
from typing import TypedDict

class LS45Data(TypedDict):
    filename: Path
    wavelength_arr: np.array
    intensity_arr: np.array


def parse(filename: Path) -> LS45Data:
    txt = filename.read_text()
    lines = txt.split("\n")
    is_data_start = False
    wavelength_arr = []
    intensity_arr = []
    for line in lines:
        if not is_data_start:
            if line == "#DATA":
                is_data_start = True
        else:
            try:
                wavelength, intensity = map(float, line.split())
                wavelength_arr.append(wavelength)
                intensity_arr.append(intensity)
            except:
                is_data_start = False
    return LS45Data(
        filename=filename,
        wavelength_arr=np.array(wavelength_arr),
        intensity_arr=np.array(intensity_arr)
    )
