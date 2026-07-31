import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";

export default function DashboardLayout() {
  return (
    <div className="flex min-h-screen bg-[var(--app-bg)]">

      <Sidebar />

      <div className="flex-1 min-w-0 flex flex-col">

        <Header />

        <main className="flex-1 overflow-y-auto">

          <div className="w-full max-w-[1600px] mx-auto px-6 py-8 lg:px-10 lg:py-10">

            <Outlet />

          </div>

        </main>

      </div>

    </div>
  );
}