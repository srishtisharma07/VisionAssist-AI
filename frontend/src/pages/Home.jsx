import { useEffect, useState } from "react";
import {
  Bot,
  Hand,
  FileText,
  Activity,
  ArrowRight,
} from "lucide-react";
import { Link } from "react-router-dom";
import { getAssistantState } from "../services/api";

export default function Home() {
  const [state, setState] = useState({
    active: false,
    status: "INACTIVE",
    last_gesture: "",
    last_command: "",
    last_tool: "",
    last_response: "",
    last_uploaded_pdf: "",
    conversation: [],
  });

  useEffect(() => {
    async function loadState() {
      const data = await getAssistantState();

      setState({
        active: data.active || false,
        status: data.status || "INACTIVE",
        last_gesture: data.last_gesture || "",
        last_command: data.last_command || "",
        last_tool: data.last_tool || "",
        last_response: data.last_response || "",
        last_uploaded_pdf: data.last_uploaded_pdf || "",
        conversation: data.conversation || [],
      });
    }

    loadState();

    const interval = setInterval(loadState, 1000);

    return () => clearInterval(interval);
  }, []);

  const statusColor = state.active
    ? "text-green-400"
    : "text-red-400";

  return (
    <div className="space-y-8">

      {/* Welcome */}

      <section>
        <p className="text-cyan-400 text-sm uppercase tracking-widest">
          Control Centre
        </p>

        <h1 className="text-4xl font-bold text-white mt-2">
          Welcome to VisionAssist AI
        </h1>

        <p className="text-slate-400 mt-3 max-w-2xl">
          Monitor your assistant, gestures, commands and document activity
          from one intelligent workspace.
        </p>
      </section>

      {/* Status Cards */}

      <section className="grid md:grid-cols-2 xl:grid-cols-4 gap-5">

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">
          <div className="flex items-center justify-between">
            <Bot className="text-cyan-400" size={28} />

            <span className={state.active ? "text-green-400" : "text-red-400"}>
              {state.active ? "ONLINE" : "OFFLINE"}
            </span>
          </div>

          <p className="text-slate-400 mt-5">
            Assistant
          </p>

          <p className={`text-2xl font-bold mt-1 ${statusColor}`}>
            {state.status}
          </p>
        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">
          <div className="flex items-center justify-between">
            <Hand className="text-green-400" size={28} />
          </div>

          <p className="text-slate-400 mt-5">
            Current Gesture
          </p>

          <p className="text-2xl font-bold text-white mt-1">
            {state.last_gesture || "--"}
          </p>
        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">
          <div className="flex items-center justify-between">
            <Activity className="text-purple-400" size={28} />
          </div>

          <p className="text-slate-400 mt-5">
            Last Tool
          </p>

          <p className="text-2xl font-bold text-white mt-1 truncate">
            {state.last_tool || "--"}
          </p>
        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">
          <div className="flex items-center justify-between">
            <FileText className="text-yellow-400" size={28} />
          </div>

          <p className="text-slate-400 mt-5">
            Conversations
          </p>

          <p className="text-2xl font-bold text-white mt-1">
            {state.conversation.length}
          </p>
        </div>

      </section>

      {/* Main Information */}

      <section className="grid lg:grid-cols-2 gap-6">

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <h2 className="text-xl font-bold text-white">
            Latest Command
          </h2>

          <div className="bg-slate-950 rounded-2xl p-5 mt-5 min-h-[120px]">

            <p className="text-cyan-400 text-sm">
              COMMAND
            </p>

            <p className="text-white text-lg mt-2">
              {state.last_command || "No command yet."}
            </p>

          </div>

          <div className="bg-slate-950 rounded-2xl p-5 mt-4">

            <p className="text-purple-400 text-sm">
              RESPONSE
            </p>

            <p className="text-slate-300 mt-2 whitespace-pre-wrap">
              {state.last_response || "No response yet."}
            </p>

          </div>

        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <h2 className="text-xl font-bold text-white">
            Quick Access
          </h2>

          <div className="grid gap-4 mt-6">

            <Link
              to="/assistant"
              className="flex items-center justify-between bg-slate-800 hover:bg-slate-700 rounded-2xl p-5 transition"
            >
              <div>
                <p className="text-white font-semibold">
                  Open Assistant
                </p>

                <p className="text-slate-400 text-sm mt-1">
                  Use gestures and voice commands
                </p>
              </div>

              <ArrowRight className="text-cyan-400" />
            </Link>

            <Link
              to="/gestures"
              className="flex items-center justify-between bg-slate-800 hover:bg-slate-700 rounded-2xl p-5 transition"
            >
              <div>
                <p className="text-white font-semibold">
                  Gesture Guide
                </p>

                <p className="text-slate-400 text-sm mt-1">
                  Learn the supported gestures
                </p>
              </div>

              <ArrowRight className="text-cyan-400" />
            </Link>

            <Link
              to="/pdf"
              className="flex items-center justify-between bg-slate-800 hover:bg-slate-700 rounded-2xl p-5 transition"
            >
              <div>
                <p className="text-white font-semibold">
                  PDF Assistant
                </p>

                <p className="text-slate-400 text-sm mt-1">
                  Upload and analyse documents
                </p>
              </div>

              <ArrowRight className="text-cyan-400" />
            </Link>

          </div>

        </div>

      </section>

    </div>
  );
}