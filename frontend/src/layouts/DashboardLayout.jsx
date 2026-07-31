import { useState } from "react";

import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";

export default function DashboardLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[var(--app-bg)]">

      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <div className="min-h-screen">

        <Header
          onMenuClick={() => setSidebarOpen(true)}
        />

        <main className="min-h-[calc(100vh-80px)] overflow-y-auto">

          <div className="w-full max-w-[1600px] mx-auto px-6 py-8 lg:px-10 lg:py-10">

            <Outlet />

          </div>

        </main>

      </div>

    </div>
  );
}