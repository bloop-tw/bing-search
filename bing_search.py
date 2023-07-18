from __future__ import annotations

import html
from typing import Any
from urllib.parse import quote

import requests
import rure
from fake_useragent import UserAgent
from pydantic import BaseModel


def bing_search(
    q: str, language: str = "en", count: int = 20
) -> dict[str, str | list[Any]]:
    ua = UserAgent()
    url = f"https://www.bing.com/search?q={quote(q)}&setlang={language}&count={count}&form=QBRE"
    res = requests.get(
        url,
        headers={
            "User-Agent": ua.random,
            "Origin": "https://www.bing.com",
            "Referer": url,
        },
    )

    results: dict[str, str | list[Any]] = {"url": url, "results": []}

    for titleContext, caption in rure.findall(
        '<li class="b_algo"[^>]*><div class="tpcn"[^>]*>.*?</div><h2>(.*?)</h2><div class="b_caption">(.*?)</div></li>',
        res.text,
    ):
        url, title = rure.findall('<a[^>]*href="(.*?)"[^>]*>(.*?)</a>', titleContext)[0]

        captionText = ""
        if snippet := rure.findall(
            '<p class="b_lineclamp.*?"><span class="algoSlug_icon"[^>]*>.*?</span>(.*?)</p>',
            caption,
        ):
            if "news_dt" in snippet[0]:
                captionText = rure.findall(
                    '<span class="news_dt">.*?</span>(.*?)$', snippet[0]
                )[0]
            else:
                captionText = snippet[0]

        results["results"].append(
            {
                "url": html.unescape(url),
                "title": html.unescape(title),
                "caption": html.unescape(captionText),
            }
        )

    return results


class Results(BaseModel):
    url: str
    results: list[WebResult]


class WebResult(BaseModel):
    url: str
    title: str
    caption: str
