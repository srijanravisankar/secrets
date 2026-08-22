import { useMutation } from "@tanstack/react-query";
import { createSecret } from "../api/secrets";

export default function useCreateSecret() {
  return useMutation({
    mutationFn: createSecret,
  });
}
