import { useState } from "react";

export default function WebcamPanel() {
  const [cameraOn, setCameraOn] = useState(false);

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

      <div className="flex items-center justify-between mb-5">

        <h2 className="text-2xl font-bold text-white">
          Live Camera
        </h2>

        <button
          onClick={() => setCameraOn(!cameraOn)}
          className="bg-cyan-500 hover:bg-cyan-400 px-5 py-2 rounded-xl text-white transition"
        >
          {cameraOn ? "Stop Camera" : "Start Camera"}
        </button>

      </div>

      <div className="rounded-2xl overflow-hidden bg-black aspect-video flex items-center justify-center">

        {cameraOn ? (
          <img
            src="http://127.0.0.1:8000/video_feed"
            alt="Camera"
            className="w-full h-full object-cover"
          />
        ) : (
          <p className="text-slate-500">
            Camera is Off
          </p>
        )}

      </div>

    </div>
  );
}