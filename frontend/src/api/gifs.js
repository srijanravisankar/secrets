import { apiRequest } from "./client";

export function searchGifs(query) {
  return apiRequest(`/gifs?q=${encodeURIComponent(query)}`);
}
