import { useEffect, useState } from "react";
import {
  Activity,
  CheckCircle2,
  Circle,
  Command,
  MessageSquare,
  MousePointer2,
} from "lucide-react";

import { getAssistantState } from "../services/api";

export default function AssistantStatus() {
  const [state, setState] = useState({
    active: false,
    status: "INACTIVE",
    last_gesture: "",
    last_command: "",
    last_tool: "",
    last_response: "",
    last_uploaded_pdf: "",
  });

  useEffect(() => {
    async function loadState() {
      const data = await getAssistantState();
      setState(data);
    }

    loadState();

    const interval = setInterval(loadState, 1000);

    return () => clearInterval(interval);
  }, []);

  const isActive = state.active;

  return (
    <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6 h-full transition-colors duration-300">

      {/* Header */}

      <div className="flex items-center justify-between mb-6">

        <div className="flex items-center gap-3">

          <div className="w-10 h-10 rounded-xl bg-[var(--accent-soft)] flex items-center justify-center">
            <Activity
              size={20}
              className="text-[var(--accent)]"
            />
          </div>

          <div>
            <h2 className="text-xl font-bold text-[var(--text-main)]">
              Assistant Status
            </h2>

            <p className="text-xs text-[var(--text-muted)] mt-1">
              Live system state
            </p>
          </div>

        </div>

        <div
          className={`flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-semibold ${
            isActive
              ? "bg-green-500/10 text-green-400"
              : "bg-[var(--panel-soft)] text-[var(--text-muted)]"
          }`}
        >
          {isActive ? (
            <CheckCircle2 size={15} />
          ) : (
            <Circle size={15} />
          )}

          {isActive ? "ACTIVE" : "INACTIVE"}
        </div>

      </div>

      {/* Status */}

      <div className="grid grid-cols-2 gap-4">

        <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            State
          </p>

          <p className="text-lg font-semibold text-[var(--accent)] mt-2">
            {state.status || "INACTIVE"}
          </p>

        </div>

        <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Gesture
          </p>

          <p className="text-lg font-semibold text-[var(--text-main)] mt-2 truncate">
            {state.last_gesture || "--"}
          </p>

        </div>

      </div>

      {/* Last Command */}

      <div className="mt-4 bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

        <div className="flex items-center gap-2">

          <Command
            size={17}
            className="text-[var(--accent)]"
          />

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Last Command
          </p>

        </div>

        <p className="text-[var(--text-main)] mt-3 leading-6">
          {state.last_command || "No command yet."}
        </p>

      </div>

      {/* Tool */}

      <div className="mt-4 bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

        <div className="flex items-center gap-2">

          <MousePointer2
            size={17}
            className="text-[var(--accent)]"
          />

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Planner Tool
          </p>

        </div>

        <p className="text-[var(--text-main)] mt-3">
          {state.last_tool || "--"}
        </p>

      </div>

      {/* Response */}

      <div className="mt-4 bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

        <div className="flex items-center gap-2">

          <MessageSquare
            size={17}
            className="text-[var(--accent)]"
          />

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Last Response
          </p>

        </div>

        <p className="text-[var(--text-main)] mt-3 whitespace-pre-wrap leading-6">
          {state.last_response || "No response yet."}
        </p>

      </div>

    </div>
  );
}