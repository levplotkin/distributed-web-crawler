import bs4

from domain.page import Page

import pytest

test_input = [
    (None, "", 0),
    ("http://a.com", "", 0),
    ("", "", 0),
    ("http://a.com", "<a href=http://a.com><a href=http://a.com>", 1),
    ("http://a.com", "<a href=http://b.com><a href=http://a.com>", 0.5),
    ("http://a.com", "<a href=http://b.com><a href=http://b.com>", 0),
    (
        "http://a.com",
        """
           <a href=http://b.com>
           <a href=http://c.com>
           <a href=http://d.com>
           <a href=http://b.com>
           """, 0
    ),
    (
        "http://a.com",
        """
           <a href=http://b.com>
           <a href=http://c.com>
           <a href=http://d.com>
           <a href=http://a.com>
           """, 0.25
    ),
]


@pytest.mark.parametrize("url,page_content,expected_rank", test_input)
def test_scanned_page_rank(url, page_content, expected_rank):
    content = bs4.BeautifulSoup(page_content, 'html.parser')
    page = Page(url=url, content=content)
    assert page.rank() == expected_rank
