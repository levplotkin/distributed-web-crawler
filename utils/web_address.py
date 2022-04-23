from urllib.parse import urlparse

import validators


def get_domain(url):
    return urlparse(url).netloc


def is_valid_url(page_address):
    return validators.url(page_address)


def is_same_domain(page_address, domain):
    return urlparse(page_address).netloc == domain
