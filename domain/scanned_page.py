from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ScannedPage:
    url: str
    depth: int
    scan_id: str
    timestamp: float
    rank: float
    hostname: str

    def __post_init__(self):
        if self.url is None or (len(self.url) == 0):
            raise ValueError("url cant be empty or None")
        if self.scan_id is None or (len(self.scan_id) == 0):
            raise ValueError("scan_id cant be empty or None")
        if self.depth is None or (self.depth) <= 0:
            raise ValueError("depth should be greater than 1")

    def key(self):
        return f"{self.scan_id}-{self.url}"
