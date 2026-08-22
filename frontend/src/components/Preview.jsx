import { fontClasses } from "../lib/fonts";

export default function Preview({
  secretMessage,
  fontStyle,
  gifUrl,
  backgroundColour,
}) {
  return (
    <div style={{ backgroundColor: backgroundColour }}>
      {gifUrl && <img src={gifUrl} alt="" />}
      <p className={fontClasses[fontStyle]}>{secretMessage}</p>
    </div>
  );
}
