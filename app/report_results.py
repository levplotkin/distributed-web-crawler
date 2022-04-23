from logging import getLogger

from domain.scanned_page import ScannedPage
from infra import db

log = getLogger(__name__)


def report_results(scan_id, output_file):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    scanned_pages = db.get_all_by_scan_id(scan_id)

    for page in scanned_pages:
        scanned_page = ScannedPage.from_json(page)

    db.remove_all()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
