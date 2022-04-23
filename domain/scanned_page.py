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

    def key(self):
        return f"{self.scan_id}-{self.url}"
