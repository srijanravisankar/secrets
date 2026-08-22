import { useQuery } from "@tanstack/react-query";
import { fetchSecretPrompt } from "../api/secrets";

export function useSecretPrompt(id) {
  return useQuery({
    queryKey: ["secret", id],
    queryFn: () => fetchSecretPrompt(id),
  });
}
