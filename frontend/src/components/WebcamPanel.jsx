import { useEffect, useState } from "react";
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
      setState(data);
    }

    const interval = setInterval(loadState, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

      <div className="flex justify-between items-center mb-5">

        <h2 className="text-2xl font-bold text-white">
          Live Camera
        </h2>

        <button
          onClick={() => setCameraOn(!cameraOn)}
          className="bg-cyan-500 hover:bg-cyan-400 text-white px-5 py-2 rounded-xl transition"
        >
          {cameraOn ? "Stop Camera" : "Start Camera"}
        </button>

      </div>

      <div className="relative rounded-2xl overflow-hidden bg-black aspect-video">

        {cameraOn ? (
          <img
            src="http://127.0.0.1:8000/video_feed"
            alt="Camera"
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="flex items-center justify-center h-full text-slate-500">
            Camera is Off
          </div>
        )}

        {cameraOn && (
          <>
            <div className="absolute top-4 left-4 bg-black/60 backdrop-blur-md px-4 py-2 rounded-xl">
              <p className="text-xs text-slate-300">
                STATUS
              </p>

              <p className="text-cyan-400 font-bold">
                {state.status || "INACTIVE"}
              </p>
            </div>

            <div className="absolute top-4 right-4 bg-black/60 backdrop-blur-md px-4 py-2 rounded-xl">
              <p className="text-xs text-slate-300">
                GESTURE
              </p>

              <p className="text-green-400 font-bold">
                {state.last_gesture || "--"}
              </p>
            </div>
          </>
        )}

      </div>

    </div>
  );
}