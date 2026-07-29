import { useState } from "react";

function WebcamPanel() {
  const [cameraStarted, setCameraStarted] = useState(false);

  return (
    <div className="bg-slate-800 rounded-xl shadow-lg p-5 h-[420px]">

      <h2 className="text-xl font-semibold text-white mb-4">
        📷 Live Camera
      </h2>

      <div className="bg-slate-900 rounded-lg h-[280px] overflow-hidden border border-slate-700">

        {cameraStarted ? (
          <img
            src="http://127.0.0.1:8000/video_feed"
            alt="Camera"
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-slate-500">
            Camera Preview
          </div>
        )}

      </div>

      <div className="mt-5 flex justify-end">

        <button
          onClick={() => setCameraStarted(true)}
          className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
        >
          {cameraStarted ? "Camera Running" : "Start Camera"}
        </button>

      </div>

    </div>
  );
}

export default WebcamPanel;