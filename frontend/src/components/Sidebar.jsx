import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Bot,
  Hand,
  FileText,
  Settings,
  X,
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

export default function Sidebar({ isOpen, onClose }) {
  return (
    <>
      {/* Background overlay */}

      {isOpen && (
        <div
          onClick={onClose}
          className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
        />
      )}

      {/* Sidebar */}

      <aside
        className={`
          fixed
          top-0
          left-0
          z-50
          h-screen
          w-72
          bg-[var(--panel-bg)]
          border-r
          border-[var(--border-color)]
          flex
          flex-col
          shadow-2xl
          transition-transform
          duration-300
          ease-in-out
          ${
            isOpen
              ? "translate-x-0"
              : "-translate-x-full"
          }
        `}
      >

        {/* Header */}

        <div className="p-7 border-b border-[var(--border-color)]">

          <div className="flex items-start justify-between">

            <div>

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

            <button
              onClick={onClose}
              className="p-2 rounded-lg text-[var(--text-muted)] hover:bg-[var(--panel-soft)] hover:text-[var(--text-main)] transition"
              aria-label="Close sidebar"
            >
              <X size={20} />
            </button>

          </div>

        </div>

        {/* Navigation */}

        <nav className="flex-1 p-5 space-y-2">

          {links.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={onClose}
                className={({ isActive }) =>
                  `flex items-center gap-4 px-5 py-4 rounded-xl transition-all duration-200 ${
                    isActive
                      ? "bg-[var(--accent)] text-white shadow-lg"
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

        {/* System Status */}

        <div className="p-5 border-t border-[var(--border-color)]">

          <div className="rounded-xl bg-[var(--panel-soft)] border border-[var(--border-color)] p-4">

            <p className="text-xs text-[var(--text-muted)]">
              SYSTEM STATUS
            </p>

            <div className="flex items-center gap-2 mt-2">

              <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />

              <p className="text-sm font-semibold text-green-500">
                System Online
              </p>

            </div>

          </div>

        </div>

      </aside>
    </>
  );
}