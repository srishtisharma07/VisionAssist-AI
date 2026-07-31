import { Cpu, Wifi, Clock, Menu, Moon, Sun } from "lucide-react";
import { useTheme } from "../context/ThemeContext";

export default function Header({ onMenuClick }) {
  const { theme, toggleTheme } = useTheme();

  return (
    <header className="sticky top-0 z-30 flex items-center justify-between px-6 py-5 lg:px-8 bg-[var(--panel-bg)] border-b border-[var(--border-color)] transition-colors duration-300">

      <div className="flex items-center gap-4">

        {/* Sidebar button */}

        <button
          onClick={onMenuClick}
          className="
            w-11
            h-11
            rounded-xl
            bg-[var(--panel-soft)]
            border
            border-[var(--border-color)]
            text-[var(--text-main)]
            flex
            items-center
            justify-center
            hover:border-[var(--accent)]
            transition
            shrink-0
          "
          aria-label="Open sidebar"
        >
          <Menu size={21} />
        </button>

        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
            VisionAssist AI
          </p>

          <h1 className="text-xl lg:text-2xl font-bold text-[var(--text-main)] mt-1">
            Intelligent Control Centre
          </h1>
        </div>

      </div>

      <div className="flex items-center gap-3 lg:gap-6">

        {/* Backend */}

        <div className="hidden md:flex items-center gap-2 text-green-500">
          <Wifi size={17} />

          <span className="text-sm">
            Backend Online
          </span>
        </div>

        {/* Assistant */}

        <div className="hidden lg:flex items-center gap-2 text-[var(--accent)]">
          <Cpu size={17} />

          <span className="text-sm">
            Assistant Ready
          </span>
        </div>

        {/* Time */}

        <div className="hidden sm:flex items-center gap-2 text-[var(--text-muted)]">
          <Clock size={17} />

          <span className="text-sm">
            {new Date().toLocaleTimeString()}
          </span>
        </div>

        {/* Theme */}

        <button
          onClick={toggleTheme}
          className="
            w-11
            h-11
            rounded-xl
            bg-[var(--panel-soft)]
            border
            border-[var(--border-color)]
            text-[var(--accent)]
            flex
            items-center
            justify-center
            hover:border-[var(--accent)]
            transition-all
            duration-300
          "
          aria-label="Toggle dark and light theme"
          title={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
        >
          {theme === "dark" ? (
            <Moon size={20} />
          ) : (
            <Sun size={20} />
          )}
        </button>

      </div>

    </header>
  );
}