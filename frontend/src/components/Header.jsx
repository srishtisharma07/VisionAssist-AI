import { Cpu, Wifi, Clock } from "lucide-react";

export default function Header() {
  return (
    <header className="flex items-center justify-between px-10 py-6 border-b border-slate-800 bg-slate-900">

      <div>

        <h1 className="text-3xl font-bold text-white">
          VisionAssist Dashboard
        </h1>

        <p className="text-slate-400">
          Gesture Controlled Agentic Personal Assistant
        </p>

      </div>

      <div className="flex items-center gap-6">

        <div className="flex items-center gap-2 text-green-400">
          <Wifi size={18} />
          <span>Backend Online</span>
        </div>

        <div className="flex items-center gap-2 text-cyan-400">
          <Cpu size={18} />
          <span>Assistant Ready</span>
        </div>

        <div className="flex items-center gap-2 text-slate-300">
          <Clock size={18} />
          <span>{new Date().toLocaleTimeString()}</span>
        </div>

      </div>

    </header>
  );
}