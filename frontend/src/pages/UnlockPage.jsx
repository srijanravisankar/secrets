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

  if (unlock.data) return <Preview {...unlock.data} />;

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>{error.message}</p>;

  const handleSubmit = (e) => {
    e.preventDefault();
    unlock.mutate(password);
  };

  return (
    <div>
      <h1>{data.secretPrompt}</h1>

      <form onSubmit={handleSubmit}>
        <input
          id="password"
          type="password"
          value={password}
          placeholder="Enter the password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="Submit">Unlock</button>
      </form>

      <div aria-live="polite">
        {unlock.isError && (
          <p>That password isn't right. You can't view this page.</p>
        )}
      </div>
    </div>
  );
}
