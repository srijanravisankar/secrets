import { fontClasses } from "../lib/fonts";

export default function Preview({
  secretMessage,
  fontStyle,
  gifUrl,
  backgroundColour,
}) {
  return (
    <div
      style={{ backgroundColor: backgroundColour }}
      className="flex h-full w-full flex-col items-center justify-center gap-6 p-8"
    >
      {gifUrl && <img src={gifUrl} alt="" className="h-96 rounded-lg" />}
      <p className={`${fontClasses[fontStyle]} text-center text-5xl`}>
        {secretMessage}
      </p>
    </div>
  );
}
