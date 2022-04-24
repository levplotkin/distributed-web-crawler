import time
from logging import getLogger

import bs4

from domain.message import Message
from domain.page import Page
from domain.scanned_page import ScannedPage
from infra import http, queue, system, db
from utils.web_address import is_valid_url

log = getLogger(__name__)


def ___url_processor(msg: Message):
    log.debug(f"url_processor {msg}")
    content = ___get_page_content(msg)
    page = Page(url=msg.url, content=content)
    scanned_page = ScannedPage(
        url=msg.url, depth=msg.depth, scan_id=msg.scan_id, timestamp=time.time(),
        rank=page.rank(), hostname=system.get_hostname(), )

    key = scanned_page.key()

    if not db.is_exist(key):
        db.insert(key, scanned_page.to_json())
        log.debug(f"db: insert {scanned_page}")
        if msg.depth > 1:
            for link in page.get_links():
                message = Message(url=link, depth=msg.depth - 1, scan_id=msg.scan_id)
                log.debug(f"queue: submit {message}")
                queue.put(message.to_json())

    else:
        log.debug(f"page {key} already exists")


def ___get_page_content(msg):
    content = ""
    if is_valid_url(msg.url):
        raw_content = http.get(msg.url)
        content = bs4.BeautifulSoup(raw_content, 'html.parser')

    return content


processors = [___url_processor]


def ___processors_callback(ch, method, properties, body):
    message = Message.from_json(body.decode('utf-8'))
    log.debug(f"message {message}")
    for processor in processors:
        processor(message)


def page_processor():
    log.info('start processors')
    queue.consume(___processors_callback)
