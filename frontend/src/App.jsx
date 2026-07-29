import { BrowserRouter, Routes, Route } from "react-router-dom";

import DashboardLayout from "./layouts/DashboardLayout";

import Home from "./pages/Home";
import Assistant from "./pages/Assistant";
import GestureGuide from "./pages/GestureGuide";
import PDFAssistant from "./pages/PDFAssistant";
import Settings from "./pages/Settings";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* Landing Page */}
        <Route path="/" element={<Home />} />

        {/* Dashboard */}
        <Route element={<DashboardLayout />}>
          <Route path="/assistant" element={<Assistant />} />
          <Route path="/gestures" element={<GestureGuide />} />
          <Route path="/pdf" element={<PDFAssistant />} />
          <Route path="/settings" element={<Settings />} />
        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;