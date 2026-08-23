import { useState } from "react";
import Preview from "../components/Preview";
import { useDebouncedValue } from "../hooks/useDebouncedValue";
import { useGifSearch } from "../hooks/useGifSearch";
import useCreateSecret from "../hooks/useCreateSecret";

export default function CreatePage() {
  const [draft, setDraft] = useState({
    secretMessage: "",
    fontStyle: "serif",
    backgroundColour: "#ffffff",
    secretPrompt: "",
    secretPassword: "",
  });

  const [gifQuery, setGifQuery] = useState("");
  const debouncedQuery = useDebouncedValue(gifQuery, 1500);
  const { data: gifData } = useGifSearch(debouncedQuery);
  const gifUrls = gifData?.urls ?? [];
  const [gifIndex, setGifIndex] = useState(0);
  const gifUrl = gifUrls[gifIndex % gifUrls.length] ?? "";

  const { mutate, data, isPending, isError, error } = useCreateSecret();

  const updateDraft = (field, value) => {
    setDraft({ ...draft, [field]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    mutate({ ...draft, gifUrl });
  };

  return (
    <div className="mx-auto grid max-w-5xl gap-8 p-8 md:grid-cols-2">
      <div>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div className="flex flex-col gap-1">
            <label
              htmlFor="secretMessage"
              className="text-sm font-medium text-gray-700"
            >
              Secret message
            </label>
            <textarea
              id="secretMessage"
              value={draft.secretMessage}
              onChange={(e) => updateDraft("secretMessage", e.target.value)}
              className="min-h-32 rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
            />
          </div>

          <div className="flex flex-col gap-1">
            <label
              htmlFor="fontStyle"
              className="text-sm font-medium text-gray-700"
            >
              Font style
            </label>
            <select
              id="fontStyle"
              name="fontStyle"
              value={draft.fontStyle}
              onChange={(e) => updateDraft("fontStyle", e.target.value)}
              className="rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
            >
              <option value="serif">Serif</option>
              <option value="sans-serif">Sans-Serif</option>
              <option value="monospace">Monospace</option>
              <option value="handwriting">Caveat</option>
              <option value="rum-raisin">Rum Raisin</option>
              <option value="henny-penny">Henny Penny</option>
            </select>
          </div>

          <div className="flex flex-col gap-1">
            <label
              htmlFor="backgroundColour"
              className="text-sm font-medium text-gray-700"
            >
              Background colour
            </label>
            <input
              id="backgroundColour"
              value={draft.backgroundColour}
              type="color"
              onChange={(e) => updateDraft("backgroundColour", e.target.value)}
              className="h-10 w-20 rounded-md border border-gray-300"
            />
          </div>

          <div className="flex flex-col gap-1">
            <label
              htmlFor="gifQuery"
              className="text-sm font-medium text-gray-700"
            >
              GIF Search
            </label>
            <div className="flex gap-2">
              <input
                id="gifQuery"
                type="text"
                maxLength="20"
                value={gifQuery}
                onChange={(e) => setGifQuery(e.target.value)}
                className="w-fit rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
              />
              <button
                type="button"
                onClick={() => setGifIndex(gifIndex + 1)}
                className="self-start rounded-md border border-gray-300 px-4 py-3 text-sm hover:bg-gray-50"
              >
                Reload GIF
              </button>
            </div>
          </div>

          <div className="flex flex-col gap-1">
            <label
              htmlFor="secretPrompt"
              className="text-sm font-medium text-gray-700"
            >
              Password prompt
            </label>
            <input
              id="secretPrompt"
              value={draft.secretPrompt}
              type="text"
              onChange={(e) => updateDraft("secretPrompt", e.target.value)}
              className="rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
            />
          </div>

          <div className="flex flex-col gap-1">
            <label
              htmlFor="secretPassword"
              className="text-sm font-medium text-gray-700"
            >
              Secret password
            </label>
            <input
              id="secretPassword"
              value={draft.secretPassword}
              type="password"
              onChange={(e) => updateDraft("secretPassword", e.target.value)}
              className="rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
            />
          </div>

          <button
            type="submit"
            disabled={!gifUrl}
            className="rounded-md bg-gray-900 px-4 py-2 text-white hover:bg-gray-800 disabled:opacity-40"
          >
            Publish
          </button>
        </form>

        {isPending && (
          <p className="mt-4 text-sm text-gray-600">Publishing...</p>
        )}
        {isError && (
          <p className="mt-4 text-sm text-red-600">{error.message}</p>
        )}
        {data && (
          <p className="mt-4 text-sm text-gray-600">
            Your Secret link:{" "}
            <a
              href={`/secret/${data.id}`}
              className="text-gray-900 underline"
            >{`${window.location.origin}/secret/${data.id}`}</a>
          </p>
        )}
      </div>

      <div className="h-full overflow-hidden rounded-xl border border-gray-200">
        <Preview {...draft} gifUrl={gifUrl} />
      </div>
    </div>
  );
}
