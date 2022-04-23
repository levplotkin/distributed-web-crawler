from logging import getLogger

import redis

from infra.config import settings

log = getLogger(__name__)

r = redis.Redis(settings.DB_HOST, settings.DB_PORT)


def is_exist(key):
    return r.exists(key) > 0


def insert(key, value):
    r.setnx(key, value)


def get_all_by_scan_id(scan_id):
    keys = r.keys(f"{scan_id}*")
    return r.mget(keys)


def remove_all():
    r.flushall()
