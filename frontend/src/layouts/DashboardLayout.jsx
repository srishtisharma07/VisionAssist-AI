import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";

function DashboardLayout() {
  return (
    <div className="flex min-h-screen bg-slate-900">

      <Sidebar />

      <main className="flex-1 overflow-auto p-8">
        <Outlet />
      </main>

    </div>
  );
}

export default DashboardLayout;