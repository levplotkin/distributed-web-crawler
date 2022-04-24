from domain.scanned_page import ScannedPage

import pytest


def test_scanned_page_key_format():
    page = ScannedPage(url="url", scan_id="scan_id", depth=1, timestamp=1, rank=1, hostname="1.2.23.3")
    key = page.key()
    assert key == "scan_id-url"


def test_scanned_empty_url():
    with pytest.raises(Exception):
        ScannedPage(url=None, scan_id="scan_id", depth=1, timestamp=1, rank=1, hostname="1.2.23.3")


def test_scanned_empty_scan_id():
    with pytest.raises(Exception):
        ScannedPage(url="url", scan_id=None, depth=1, timestamp=1, rank=1, hostname="1.2.23.3")


def test_scanned_blank_url():
    with pytest.raises(Exception):
        ScannedPage(url="", scan_id="scan_id", depth=1, timestamp=1, rank=1, hostname="1.2.23.3")


def test_scanned_blank_scan_id():
    with pytest.raises(Exception):
        ScannedPage(url="url", scan_id="", depth=1, timestamp=1, rank=1, hostname="1.2.23.3")


def test_scanned_depth_less_0():
    with pytest.raises(Exception):
        ScannedPage(url="url", scan_id="scan_id", depth=0, timestamp=1, rank=1, hostname="1.2.23.3")
