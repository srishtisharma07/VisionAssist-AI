import { useEffect, useState } from "react";
import {
  Camera,
  Circle,
  Hand,
  Play,
  Square,
} from "lucide-react";

import { getAssistantState } from "../services/api";

export default function WebcamPanel() {
  const [cameraOn, setCameraOn] = useState(false);

  const [state, setState] = useState({
    status: "INACTIVE",
    last_gesture: "",
  });

  useEffect(() => {
    async function loadState() {
      const data = await getAssistantState();

      setState({
        status: data.status || "INACTIVE",
        last_gesture: data.last_gesture || "",
      });
    }

    loadState();

    const interval = setInterval(loadState, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6 transition-colors duration-300">

      {/* Header */}

      <div className="flex items-center justify-between mb-5">

        <div className="flex items-center gap-3">

          <div className="w-10 h-10 rounded-xl bg-[var(--accent-soft)] flex items-center justify-center">
            <Camera
              size={20}
              className="text-[var(--accent)]"
            />
          </div>

          <div>
            <h2 className="text-xl font-bold text-[var(--text-main)]">
              Live Camera
            </h2>

            <p className="text-xs text-[var(--text-muted)] mt-1">
              Gesture recognition feed
            </p>
          </div>

        </div>

        <button
          onClick={() => setCameraOn((current) => !current)}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl font-semibold transition ${
            cameraOn
              ? "bg-red-500 text-white hover:bg-red-600"
              : "bg-[var(--accent)] text-white hover:opacity-90"
          }`}
        >
          {cameraOn ? (
            <>
              <Square size={16} />
              Stop Camera
            </>
          ) : (
            <>
              <Play size={16} />
              Start Camera
            </>
          )}
        </button>

      </div>

      {/* Camera */}

      <div className="relative rounded-2xl overflow-hidden bg-black aspect-video border border-[var(--border-color)]">

        {cameraOn ? (
          <img
            src="http://127.0.0.1:8000/video_feed"
            alt="VisionAssist live camera"
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="flex flex-col items-center justify-center h-full text-center">

            <Camera
              size={42}
              className="text-[var(--text-muted)]"
            />

            <p className="text-[var(--text-muted)] mt-4">
              Camera is off
            </p>

            <p className="text-[var(--text-muted)] text-sm mt-1 opacity-70">
              Start the camera to begin gesture recognition.
            </p>

          </div>
        )}

        {/* Live Overlays */}

        {cameraOn && (
          <>
            <div className="absolute top-4 left-4 bg-black/70 backdrop-blur-md rounded-xl px-4 py-3 border border-white/10">

              <p className="text-[10px] uppercase tracking-widest text-slate-300">
                Assistant State
              </p>

              <div className="flex items-center gap-2 mt-1">

                <Circle
                  size={9}
                  fill="currentColor"
                  className={
                    state.status === "INACTIVE"
                      ? "text-red-400"
                      : "text-green-400"
                  }
                />

                <p className="text-sm font-semibold text-white">
                  {state.status || "INACTIVE"}
                </p>

              </div>

            </div>

            <div className="absolute top-4 right-4 bg-black/70 backdrop-blur-md rounded-xl px-4 py-3 border border-white/10">

              <div className="flex items-center gap-2">

                <Hand
                  size={15}
                  className="text-[var(--accent)]"
                />

                <p className="text-[10px] uppercase tracking-widest text-slate-300">
                  Gesture
                </p>

              </div>

              <p className="text-sm font-semibold text-white mt-1">
                {state.last_gesture || "--"}
              </p>

            </div>
          </>
        )}

      </div>

      {/* Bottom Info */}

      <div className="grid grid-cols-2 gap-4 mt-4">

        <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Current Gesture
          </p>

          <p className="text-lg font-semibold text-[var(--text-main)] mt-2">
            {state.last_gesture || "--"}
          </p>

        </div>

        <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-4">

          <p className="text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Assistant State
          </p>

          <p className="text-lg font-semibold text-[var(--accent)] mt-2">
            {state.status || "INACTIVE"}
          </p>

        </div>

      </div>

    </div>
  );
}