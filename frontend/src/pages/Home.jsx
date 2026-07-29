export default function Home() {
  return (
    <div className="p-10">

      <h1 className="text-4xl font-bold text-white">
        VisionAssist Dashboard
      </h1>

      <p className="text-slate-400 mt-2">
        Gesture Controlled Agentic Personal Assistant
      </p>

      <div className="grid grid-cols-4 gap-6 mt-10">

        <div className="bg-slate-800 rounded-xl p-6">
          <p className="text-slate-400">Assistant</p>
          <h2 className="text-2xl text-green-400 font-bold mt-3">
            Ready
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6">
          <p className="text-slate-400">Gesture</p>
          <h2 className="text-2xl text-blue-400 font-bold mt-3">
            None
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6">
          <p className="text-slate-400">Last Tool</p>
          <h2 className="text-2xl text-purple-400 font-bold mt-3">
            —
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6">
          <p className="text-slate-400">Commands</p>
          <h2 className="text-2xl text-yellow-400 font-bold mt-3">
            0
          </h2>
        </div>

      </div>

    </div>
  );
}