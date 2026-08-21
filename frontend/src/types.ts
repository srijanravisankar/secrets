export type FontStyle = "serif" | "sans-serif" | "monospace";

export interface SecretContent {
  secret_message: string;
  font_style: FontStyle;
  gif_url: string;
  background_colour: string;
}

export interface SecretCreateRequest extends SecretContent {
  secret_prompt: string;
  secret_password: string;
}

export interface SecretCreateResponse {
  id: string;
}

export interface SecretPromptResponse {
  secret_prompt: string;
}

export interface SecretReadRequest {
  secret_password: string;
}

export type SecretReadResponse = SecretContent;
