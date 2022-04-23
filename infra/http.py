from logging import getLogger

import requests

log = getLogger(__name__)


def get_status(scheme: str, address: str):
    try:
        return requests.get(f'{scheme}://{address}')
    except requests.exceptions.HTTPError as err:
        log.error(err)
        return None


def get(url: str):
    try:
        return requests.get(url).text
    except requests.exceptions.HTTPError as err:
        log.error(err)
        return None
