import { Route, Routes } from "react-router-dom";

import CreatePage from "./pages/CreatePage";
import UnlockPage from "./pages/UnlockPage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<CreatePage />} />
      <Route path="/secret/:id" element={<UnlockPage />} />
    </Routes>
  );
}
