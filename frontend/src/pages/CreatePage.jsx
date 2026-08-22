import { useState } from "react";
import Preview from "../components/Preview";

export default function CreatePage() {
  const [draft, setDraft] = useState({
    secretMessage: "",
    fontStyle: "serif",
    gifUrl: "",
    backgroundColour: "#ffffff",
    secretPrompt: "",
    secretPassword: "",
  });

  const updateDraft = (field, value) => {
    setDraft({ ...draft, [field]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="secretMessage">Secret Message: </label>
          <textarea
            id="secretMessage"
            value={draft.secretMessage}
            onChange={(e) => updateDraft("secretMessage", e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="fontStyle">Choose a font style: </label>
          <select
            id="fontStyle"
            name="fontStyle"
            value={draft.fontStyle}
            onChange={(e) => updateDraft("fontStyle", e.target.value)}
          >
            <option value="serif">Serif</option>
            <option value="sans-serif">Sans-Serif</option>
            <option value="monospace">Monospace</option>
          </select>
        </div>

        <div>
          <label htmlFor="backgroundColour">Choose a Background Colour: </label>
          <input
            id="backgroundColour"
            value={draft.backgroundColour}
            type="color"
            onChange={(e) => updateDraft("backgroundColour", e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="secretPrompt">Choose a prompt for secret: </label>
          <input
            id="secretPrompt"
            value={draft.secretPrompt}
            type="text"
            onChange={(e) => updateDraft("secretPrompt", e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="secretPassword">Choose a password for secret: </label>
          <input
            id="secretPassword"
            value={draft.secretPassword}
            type="password"
            onChange={(e) => updateDraft("secretPassword", e.target.value)}
          />
        </div>

        <button type="submit">Publish</button>
      </form>

      <Preview {...draft} />
    </div>
  );
}
