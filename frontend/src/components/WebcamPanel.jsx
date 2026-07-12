function WebcamPanel() {
  return (
    <div className="bg-slate-800 rounded-xl shadow-lg p-5 h-[420px]">

      <h2 className="text-xl font-semibold text-white mb-4">
        📷 Live Camera
      </h2>

      <div className="bg-slate-900 rounded-lg h-[280px] flex items-center justify-center border border-slate-700">

        <p className="text-slate-500">
          Camera Preview
        </p>

      </div>

      <div className="mt-5 flex justify-between">

        <div>

          <p className="text-slate-400 text-sm">
            Current Gesture
          </p>

          <p className="text-green-400 text-xl font-bold">
            None
          </p>

        </div>

        <button
          className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
        >
          Start Camera
        </button>

      </div>

    </div>
  );
}

export default WebcamPanel;