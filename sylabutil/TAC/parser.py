import numpy as np
import numpy.typing as npt

import enum
from pathlib import Path
import re
from typing import TypedDict, Dict, List

class TACData(TypedDict):
    info: Dict[str, str]
    block: Dict[str, Dict[str, npt.NDArray]]

class FileBlock(enum.Enum):
    INFO_BLOCK = 0
    DATA_BLOCK = 1

def parse(filename: Path) -> TACData:
    data: TACData = {
        "info": dict(),
        "block": dict()
    }
    current_state: FileBlock = FileBlock.INFO_BLOCK
    block_name = "0"
    data_line_property_names: List[str] = []
    data_line_property_values: List[List[float]] = []
    with filename.open("rt") as f:
        for line in f.readlines():
            if line.startswith("*BLOCK"):
                current_state = FileBlock.DATA_BLOCK
                m = re.fullmatch(r"\*BLOCK\s+(.*?)\s+\(\s+(.*?)\s+\)\n", line)
                assert m is not None, f"Unexpected file format or code is broken, {line}"
                block_name = m.group(1)
                data_line_property_names = list(m.group(2).split())
                data_line_property_values = [[] for _ in data_line_property_names]
                continue
            elif line.startswith("*END"):
                if current_state == FileBlock.DATA_BLOCK:
                    data["block"][block_name] = {
                        key: np.array(value)
                        for key, value in zip(data_line_property_names, data_line_property_values)
                    }
                    
                current_state = FileBlock.INFO_BLOCK
                continue

            if current_state == FileBlock.INFO_BLOCK:
                try:
                    key, value = map(lambda s: s.strip(), line.split(":"))
                    data["info"][key] = value
                except:
                    continue
            elif current_state == FileBlock.DATA_BLOCK:
                try:
                    values = tuple(map(lambda s: float(s), line.split()))
                    for i in range(len(data_line_property_values)):
                        data_line_property_values[i].append(values[i])
                except:
                    continue

    return data