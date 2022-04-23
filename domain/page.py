import typing
from logging import getLogger

import bs4
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from utils.web_address import get_domain, is_valid_url, is_same_domain

log = getLogger(__name__)


@dataclass_json
@dataclass
class Page:
    url: str
    content: bs4.BeautifulSoup

    def rank(self) -> float:
        "Calculate the rank of the page as ratio of same domain links to all links"
        domain = get_domain(self.url)
        all_links = self.___get_all_links()
        external_links = self.___get_external_links(all_links, domain)

        external_links_count = len(external_links)
        all_links_count = len(all_links)
        rank = 0 if all_links_count == 0 else (all_links_count - external_links_count) / all_links_count
        return rank

    def ___get_external_links(self, urls: typing.List[str], domain: str) -> typing.List[str]:
        return list(filter(lambda url: is_valid_url(url) and not is_same_domain(url, domain), urls))

    def ___get_all_links(self) -> typing.List[str]:
        try:
            html_anchors = self.content.find_all('a')
            links = [attributes['href'] for attributes in html_anchors]
        except (KeyError, AttributeError):
            log.error("KeyError: 'href' not found in html_anchors")
            links = []

        return links

    def get_links(self) -> typing.List[str]:
        return self.___get_all_links()
