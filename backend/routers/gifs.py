from fastapi import APIRouter
from schemas.gifs import GifSearchResponse
from services import giphy

router = APIRouter(prefix="/gifs")


@router.get("", response_model=GifSearchResponse)
def search_gifs(q: str) -> GifSearchResponse:
    gif_urls = giphy.search_gifs(q)
    return GifSearchResponse(urls=gif_urls)
