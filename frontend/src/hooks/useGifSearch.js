import { useQuery } from "@tanstack/react-query";
import { searchGifs } from "../api/gifs";

export function useGifSearch(query) {
  return useQuery({
    queryKey: ["gifs", query],
    queryFn: () => searchGifs(query),
    enabled: query.length > 0,
  });
}
