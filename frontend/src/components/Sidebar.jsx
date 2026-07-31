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
    <aside className="w-72 min-h-screen bg-[var(--panel-bg)] border-r border-[var(--border-color)] flex flex-col transition-colors duration-300">

      <div className="p-8 border-b border-[var(--border-color)]">

        <p className="text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
          AI Control System
        </p>

        <h1 className="text-2xl font-bold text-[var(--text-main)] mt-2">
          VisionAssist
        </h1>

        <p className="text-sm text-[var(--text-muted)] mt-1">
          Gesture AI Assistant
        </p>

      </div>

      <nav className="flex-1 p-5 space-y-2">

        {links.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-4 px-5 py-4 rounded-xl transition-all duration-200 ${
                  isActive
                    ? "bg-[var(--accent)] text-white shadow-lg shadow-black/20"
                    : "text-[var(--text-muted)] hover:bg-[var(--panel-soft)] hover:text-[var(--text-main)]"
                }`
              }
            >
              <Icon size={21} />
              <span className="font-medium">
                {item.name}
              </span>
            </NavLink>
          );
        })}

      </nav>

      <div className="p-5 border-t border-[var(--border-color)]">

        <div className="rounded-xl bg-[var(--panel-soft)] border border-[var(--border-color)] p-4">

          <p className="text-xs text-[var(--text-muted)]">
            SYSTEM STATUS
          </p>

          <div className="flex items-center gap-2 mt-2">
            <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />

            <p className="text-sm font-semibold text-green-400">
              System Online
            </p>
          </div>

        </div>

      </div>

    </aside>
  );
}