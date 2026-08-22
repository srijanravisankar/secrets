import { useParams } from "react-router-dom";
import { useSecretPrompt } from "../hooks/useSecretPrompt";
import { useState } from "react";

import Preview from "../components/Preview";
import { useUnlockSecret } from "../hooks/useUnlockSecret";

export default function UnlockPage() {
  const { id } = useParams();
  const { data, isLoading, isError, error } = useSecretPrompt(id);

  const [password, setPassword] = useState("");
  const unlock = useUnlockSecret(id);

  if (unlock.data) {
    return (
      <div className="h-screen">
        <Preview {...unlock.data} />;
      </div>
    );
  }

  if (isLoading)
    return (
      <p className="flex h-screen items-center justify-center text-sm text-gray-600">
        Loading...
      </p>
    );
  if (isError)
    return (
      <p className="flex h-screen items-center justify-center text-sm text-red-600">
        {error.message}
      </p>
    );

  const handleSubmit = (e) => {
    e.preventDefault();
    unlock.mutate(password);
  };

  return (
    <div className="flex h-screen items-center justify-center p-8">
      <div className="w-full max-w-sm">
        <h1 className="text-center text-xl font-medium text-gray-900">
          {data.secretPrompt}
        </h1>

        <form onSubmit={handleSubmit} className="mt-6 flex flex-col gap-3">
          <input
            id="password"
            type="password"
            value={password}
            placeholder="Enter the password"
            onChange={(e) => setPassword(e.target.value)}
            className="rounded-md border border-gray-300 px-3 py-2 focus:border-gray-900 focus:outline-none"
          />

          <button
            type="Submit"
            className="rounded-md bg-gray-900 px-4 py-2 text-white hover:bg-gray-800"
          >
            Unlock
          </button>
        </form>

        <div aria-live="polite">
          {unlock.isError && (
            <p className="mt-4 text-center text-sm text-red-600">
              That password isn't right. You can't view this page.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
