export type FontStyle = "serif" | "sans-serif" | "monospace";

export interface SecretContent {
  secretMessage: string;
  fontStyle: FontStyle;
  gifUrl: string;
  backgroundColour: string;
}

export interface SecretCreateRequest extends SecretContent {
  secretPrompt: string;
  secretPassword: string;
}

export interface SecretCreateResponse {
  id: string;
}

export interface SecretPromptResponse {
  secretPrompt: string;
}

export interface SecretReadRequest {
  secretPassword: string;
}

export type SecretReadResponse = SecretContent;
