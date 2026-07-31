import { useEffect, useState } from "react";
import {
  Server,
  Camera,
  Mic,
  Brain,
  FileText,
  CheckCircle2,
  XCircle,
} from "lucide-react";

import { getAssistantState, getPdfInfo } from "../services/api";

export default function Settings() {
  const [backendOnline, setBackendOnline] = useState(false);

  const [state, setState] = useState({
    status: "INACTIVE",
  });

  const [pdfInfo, setPdfInfo] = useState({
    total_pdfs: 0,
  });

  useEffect(() => {
    async function loadSystemInfo() {
      try {
        const assistantState = await getAssistantState();

        setState(assistantState);
        setBackendOnline(true);
      } catch (error) {
        console.error(error);
        setBackendOnline(false);
      }

      const info = await getPdfInfo();
      setPdfInfo(info);
    }

    loadSystemInfo();

    const interval = setInterval(loadSystemInfo, 3000);

    return () => clearInterval(interval);
  }, []);

  const StatusBadge = ({ online }) => (
    <div
      className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm ${
        online
          ? "bg-green-500/10 text-green-400"
          : "bg-red-500/10 text-red-400"
      }`}
    >
      {online ? (
        <CheckCircle2 size={16} />
      ) : (
        <XCircle size={16} />
      )}

      {online ? "Online" : "Offline"}
    </div>
  );

  return (
    <div className="space-y-8">

      <section>
        <p className="text-cyan-400 text-sm uppercase tracking-[0.2em]">
          System Configuration
        </p>

        <h1 className="text-4xl font-bold text-white mt-2">
          Settings
        </h1>

        <p className="text-slate-400 mt-3">
          Monitor the VisionAssist AI environment and connected services.
        </p>
      </section>

      {/* System Status */}

      <section className="grid md:grid-cols-2 gap-6">

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <div className="flex items-start justify-between">

            <div className="flex items-center gap-4">
              <Server className="text-green-400" size={28} />

              <div>
                <h2 className="text-xl font-bold text-white">
                  Backend
                </h2>

                <p className="text-slate-400 text-sm mt-1">
                  FastAPI service
                </p>
              </div>
            </div>

            <StatusBadge online={backendOnline} />

          </div>

          <div className="mt-6 bg-slate-950 rounded-2xl p-4">
            <p className="text-slate-400 text-sm">
              Endpoint
            </p>

            <p className="text-white mt-1 font-mono">
              http://127.0.0.1:8000
            </p>
          </div>

        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <div className="flex items-center gap-4">
            <Camera className="text-cyan-400" size={28} />

            <div>
              <h2 className="text-xl font-bold text-white">
                Camera
              </h2>

              <p className="text-slate-400 text-sm mt-1">
                Gesture recognition input
              </p>
            </div>
          </div>

          <div className="mt-6 bg-slate-950 rounded-2xl p-4">
            <p className="text-slate-400 text-sm">
              Stream
            </p>

            <p className="text-green-400 mt-1">
              Available
            </p>
          </div>

        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <div className="flex items-center gap-4">
            <Mic className="text-purple-400" size={28} />

            <div>
              <h2 className="text-xl font-bold text-white">
                Voice
              </h2>

              <p className="text-slate-400 text-sm mt-1">
                Speech recognition and response
              </p>
            </div>
          </div>

          <div className="mt-6 bg-slate-950 rounded-2xl p-4">
            <p className="text-slate-400 text-sm">
              Assistant status
            </p>

            <p className="text-cyan-400 mt-1 font-semibold">
              {state.status || "INACTIVE"}
            </p>
          </div>

        </div>

        <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

          <div className="flex items-center gap-4">
            <Brain className="text-yellow-400" size={28} />

            <div>
              <h2 className="text-xl font-bold text-white">
                AI Agent
              </h2>

              <p className="text-slate-400 text-sm mt-1">
                Planner and tool orchestration
              </p>
            </div>
          </div>

          <div className="mt-6 bg-slate-950 rounded-2xl p-4">

            <p className="text-slate-400 text-sm">
              Last planner tool
            </p>

            <p className="text-white mt-1">
              {state.last_tool || "--"}
            </p>

          </div>

        </div>

      </section>

      {/* Project Information */}

      <section className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

        <div className="flex items-center gap-4">

          <FileText className="text-cyan-400" size={28} />

          <div>
            <h2 className="text-xl font-bold text-white">
              Document Workspace
            </h2>

            <p className="text-slate-400 text-sm mt-1">
              Current PDF workspace status
            </p>
          </div>

        </div>

        <div className="grid md:grid-cols-3 gap-4 mt-6">

          <div className="bg-slate-950 rounded-2xl p-5">
            <p className="text-slate-400 text-sm">
              Uploaded PDFs
            </p>

            <p className="text-2xl font-bold text-cyan-400 mt-2">
              {pdfInfo.total_pdfs}
            </p>
          </div>

          <div className="bg-slate-950 rounded-2xl p-5">
            <p className="text-slate-400 text-sm">
              Frontend
            </p>

            <p className="text-2xl font-bold text-green-400 mt-2">
              React
            </p>
          </div>

          <div className="bg-slate-950 rounded-2xl p-5">
            <p className="text-slate-400 text-sm">
              Backend
            </p>

            <p className="text-2xl font-bold text-purple-400 mt-2">
              FastAPI
            </p>
          </div>

        </div>

      </section>

    </div>
  );
}