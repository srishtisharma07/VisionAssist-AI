import { Cpu, Wifi, Clock } from "lucide-react";

export default function Header() {
  return (
    <header className="flex items-center justify-between px-8 py-5 bg-[var(--panel-bg)] border-b border-[var(--border-color)] transition-colors duration-300">

      <div>
        <p className="text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
          VisionAssist AI
        </p>

        <h1 className="text-2xl font-bold text-[var(--text-main)] mt-1">
          Intelligent Control Centre
        </h1>
      </div>

      <div className="flex items-center gap-6">

        <div className="flex items-center gap-2 text-green-500">
          <Wifi size={17} />
          <span className="text-sm">
            Backend Online
          </span>
        </div>

        <div className="flex items-center gap-2 text-[var(--accent)]">
          <Cpu size={17} />
          <span className="text-sm">
            Assistant Ready
          </span>
        </div>

        <div className="flex items-center gap-2 text-[var(--text-muted)]">
          <Clock size={17} />
          <span className="text-sm">
            {new Date().toLocaleTimeString()}
          </span>
        </div>

      </div>

    </header>
  );
}