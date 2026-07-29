import { useEffect, useState } from "react";
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

  const statusColor = state.active
    ? "text-green-400"
    : "text-red-400";

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6 h-full">

      <h2 className="text-2xl font-bold text-white mb-6">
        Assistant Status
      </h2>

      <div className="space-y-5">

        <div className="flex items-center justify-between">
          <span className="text-slate-400">
            Status
          </span>

          <span className={`font-bold ${statusColor}`}>
            {state.status || "INACTIVE"}
          </span>
        </div>

        <div className="flex items-center justify-between">
          <span className="text-slate-400">
            Active
          </span>

          <span className={state.active ? "text-green-400" : "text-red-400"}>
            {state.active ? "🟢 Yes" : "🔴 No"}
          </span>
        </div>

        <div className="flex items-center justify-between">
          <span className="text-slate-400">
            Gesture
          </span>

          <span className="text-white font-semibold">
            {state.last_gesture || "--"}
          </span>
        </div>

        <div>
          <p className="text-slate-400 mb-2">
            Last Command
          </p>

          <div className="bg-slate-800 rounded-xl p-3 text-white min-h-[60px]">
            {state.last_command || "--"}
          </div>
        </div>

        <div>
          <p className="text-slate-400 mb-2">
            Planner Tool
          </p>

          <div className="bg-slate-800 rounded-xl p-3 text-white min-h-[50px]">
            {state.last_tool || "--"}
          </div>
        </div>

        <div>
          <p className="text-slate-400 mb-2">
            Last Response
          </p>

          <div className="bg-slate-800 rounded-xl p-3 text-white whitespace-pre-wrap min-h-[100px]">
            {state.last_response || "--"}
          </div>
        </div>

        <div>
          <p className="text-slate-400 mb-2">
            Uploaded PDF
          </p>

          <div className="bg-slate-800 rounded-xl p-3 text-white">
            {state.last_uploaded_pdf || "--"}
          </div>
        </div>

      </div>

    </div>
  );
}