from dataclasses import fields, asdict
from logging import getLogger
import csv
from domain.scanned_page import ScannedPage
from infra import db
import os

log = getLogger(__name__)


def report_results(scan_id, output_file):
    header = get_scanned_page_fields()
    rows = get_report_rows(scan_id)

    with open(output_file, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(header)
        tsv_writer.writerows(rows)

    db.remove_all()
    abspath = os.path.abspath(output_file)
    log.info(f"report for scan {scan_id} is saved in {abspath}")


def get_report_rows(scan_id):
    scanned_pages = db.get_all_by_scan_id(scan_id)
    for page in scanned_pages:
        scanned_page = ScannedPage.from_json(page)
        yield get_report_row(scanned_page)


def get_report_row(scanned_page):
    result = []
    fields = get_scanned_page_fields()
    scanned_page_dict = asdict(scanned_page)
    for field_name in fields:
        result.append(scanned_page_dict[field_name])
    return result


def get_scanned_page_fields():
    return [field.name for field in fields(ScannedPage)]
