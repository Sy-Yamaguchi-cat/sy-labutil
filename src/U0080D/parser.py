from .xlrd import xlrd
import numpy as np
from pathlib import Path
from typing import TypedDict

class U0080DData(TypedDict):
    points: int
    wavelength: np.array
    data: np.array

class U0080DFile(TypedDict):
    filename: Path

    start_wavelength: int
    interval: int
    points: int

    data: U0080DData


def parse(filename: Path) -> U0080DFile:
    workbook = xlrd.open_workbook(filename)
    sheets = workbook.sheets()
    sheet: xlrd.sheet.Sheet = sheets[0]

    start_wavelength = int(sheet.cell_value(0, 0))
    interval = int(sheet.cell_value(1, 0))
    points = int(sheet.cell_value(2, 0))

    wavelength_arr = np.empty(points, np.float64)
    data_arr = np.empty(points, np.float64)

    for i in range(points):
        wavelength = float(sheet.cell_value(5+i, 0))
        data = float(sheet.cell_value(5+i, 1))
        wavelength_arr[i] = wavelength
        data_arr[i] = data

    return U0080DFile(
        filename=filename,
        start_wavelength=start_wavelength,
        interval=interval,
        points=points,
        data=U0080DData(
            wavelength=wavelength_arr,
            data=data_arr
        )
    )
