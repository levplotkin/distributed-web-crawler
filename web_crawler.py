import logging
from logging import getLogger

import click

from app.page_processor import page_processor
from app.report_results import report_results
from app.seed_url import seed_url
from infra.config import settings
from utils.cli_validator import validate_positive_int, validate_url

log = getLogger(__name__)


@click.group()
def seed():
    pass


@click.group()
def processor():
    pass


@click.group()
def report():
    pass


@seed.command()
@click.option('--root', help='url to crawl', required=True, type=str, callback=validate_url)
@click.option('--depth', help='recursion depth limit, --depth 1 meaning only root page will be scanned  ',
              required=True, type=int, callback=validate_positive_int, )
def start_crawler(root: str, depth: int):
    seed_url(depth, root)


@processor.command()
def start_processor():
    page_processor()


@report.command()
@click.option('--scan-id', help='scan id', type=str, required=True)
@click.option('--output', help='path to output file', type=str, required=True)
def save_report(scan_id: str, output: str):
    report_results(scan_id, output)


cli = click.CommandCollection(sources=[seed, processor, report])
if __name__ == "__main__":
    logging_level = logging.getLevelName(settings.LOG_LEVEL)
    logging.basicConfig(level=logging_level)

    cli()
