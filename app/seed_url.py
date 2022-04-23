import uuid
from logging import getLogger

from domain.message import Message
from infra.queue import put

log = getLogger(__name__)


def seed_url(depth, root):
    log.info('seed_url  >>>>>>>>>>>>>>>> ')
    message = Message(depth=depth, url=root, scan_id=uuid.uuid4().hex)

    put(message.to_json())
