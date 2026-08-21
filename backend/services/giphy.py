import os

import httpx2
from dotenv import load_dotenv

load_dotenv()

GIPHY_API_KEY = os.environ["GIPHY_API_KEY"]


def search_gifs(query: str) -> list[str]:
    giphy_result = (
        httpx2.get(
            "https://api.giphy.com/v1/gifs/search",
            params={
                "api_key": GIPHY_API_KEY,
                "q": query,
                "limit": 5,
            },
        )
        .raise_for_status()
        .json()
    )

    gifs_urls = []
    for gif_data in giphy_result["data"]:
        gifs_urls.append(gif_data["images"]["original"]["url"])

    return gifs_urls
