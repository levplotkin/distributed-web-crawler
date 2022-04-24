import uuid
from logging import getLogger

from domain.message import Message
from infra.queue import put

log = getLogger(__name__)


def seed_url(depth, root):
    scan_id = uuid.uuid4().hex
    message = Message(depth=depth, url=root, scan_id=scan_id)
    log.info(f'start web crawler {message}')
    put(message.to_json())
