import { useMutation } from "@tanstack/react-query";
import { unlockSecret } from "../api/secrets";

export function useUnlockSecret(id) {
  return useMutation({
    mutationFn: (secretPassword) => unlockSecret(id, secretPassword),
  });
}
