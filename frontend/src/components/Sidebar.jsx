import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Bot,
  Hand,
  FileText,
  Settings,
} from "lucide-react";

const links = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Assistant",
    path: "/assistant",
    icon: Bot,
  },
  {
    name: "Gestures",
    path: "/gestures",
    icon: Hand,
  },
  {
    name: "PDF Assistant",
    path: "/pdf",
    icon: FileText,
  },
  {
    name: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-slate-950 border-r border-slate-800 flex flex-col">

      <div className="p-8 border-b border-slate-800">

        <h1 className="text-3xl font-bold text-white">
          VisionAssist
        </h1>

        <p className="text-slate-400 mt-2">
          Gesture AI Assistant
        </p>

      </div>

      <nav className="flex-1 p-5 space-y-2">

        {links.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-4 px-5 py-4 rounded-xl transition-all duration-200 ${
                  isActive
                    ? "bg-blue-600 text-white shadow-lg"
                    : "text-slate-300 hover:bg-slate-800 hover:text-white"
                }`
              }
            >
              <Icon size={22} />
              <span className="font-medium">
                {item.name}
              </span>
            </NavLink>
          );
        })}

      </nav>

      <div className="p-5 border-t border-slate-800">

        <div className="rounded-xl bg-slate-900 p-4">

          <p className="text-sm text-slate-400">
            VisionAssist AI
          </p>

          <p className="text-green-400 font-semibold">
            System Online
          </p>

        </div>

      </div>

    </aside>
  );
}