from dataclasses import dataclass
from typing import Optional

@dataclass
class Package:
    pid: str
    weight: int
    value: float
    destination: str
    priority: Optional[int] = 0

@dataclass
class Van:
    vid: str
    capacity: int
    start: str = "DEPOT"
