import csv
from pathlib import Path
import numpy as np

import numpy.typing as npt
from typing import List, TypedDict


class Spectram(TypedDict):
    title: str
    wavelength: npt.NDArray[np.float64]
    transmittance: npt.NDArray[np.float64]


def parse(filename: Path) -> Spectram:
    wavelength_arr: List[float] = []
    transmittance_arr: List[float] = []
    with filename.open("rt") as f:
        # read title line
        title: str = f.readline().strip().strip('"')
        # skip header line
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            wavelength, transmittance = map(float, row)
            wavelength_arr.append(wavelength)
            transmittance_arr.append(transmittance)
    return Spectram(
        title=title,
        wavelength=np.array(wavelength_arr),
        transmittance=np.array(transmittance_arr),
    )
