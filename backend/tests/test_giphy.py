from services import giphy


class FakeResponse:
    def raise_for_status(self):
        return self

    def json(self):
        return {
            "data": [
                {
                    "url": "https://giphy.com/gifs/page-one",
                    "images": {"original": {"url": "https://media.giphy.com/one.gif"}},
                }
            ]
        }


def test_search_gifs_returns_original_image_urls(monkeypatch):
    monkeypatch.setattr(giphy.httpx2, "get", lambda *args, **kwargs: FakeResponse())
    gif_urls = giphy.search_gifs("cats")
    assert gif_urls == ["https://media.giphy.com/one.gif"]
