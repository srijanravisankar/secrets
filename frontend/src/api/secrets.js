import { apiRequest } from "./client";

export function createSecret(secret) {
  return apiRequest(`/secrets`, {
    method: "POST",
    body: JSON.stringify(secret),
  });
}

export function fetchSecretPrompt(id) {
  return apiRequest(`/secrets/${id}`);
}

export function unlockSecret(id, secretPassword) {
  return apiRequest(`/secrets/${id}/unlock`, {
    method: "POST",
    body: JSON.stringify({ secretPassword }),
  });
}
