const gestures = [
  {
    emoji: "🖐",
    name: "OPEN PALM",
    action: "Activate Assistant",
    color: "border-green-500",
  },
  {
    emoji: "☝",
    name: "INDEX",
    action: "Start Listening",
    color: "border-cyan-500",
  },
  {
    emoji: "👍",
    name: "THUMBS UP",
    action: "Confirm Voice Command",
    color: "border-blue-500",
  },
  {
    emoji: "👎",
    name: "THUMBS DOWN",
    action: "Retry Voice Command",
    color: "border-yellow-500",
  },
  {
    emoji: "✊",
    name: "FIST",
    action: "Deactivate Assistant",
    color: "border-red-500",
  },
  {
    emoji: "✌",
    name: "VICTORY",
    action: "Reserved For Future",
    color: "border-purple-500",
  },
];

export default function GestureGuide() {
  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold text-white">
          Gesture Guide
        </h1>

        <p className="text-slate-400 mt-2">
          Learn the supported hand gestures for controlling VisionAssist AI.
        </p>
      </div>

      <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-6">

        {gestures.map((gesture) => (
          <div
            key={gesture.name}
            className={`bg-slate-900 rounded-3xl border ${gesture.color} p-6 hover:scale-105 transition-all duration-300`}
          >

            <div className="text-6xl mb-5">
              {gesture.emoji}
            </div>

            <h2 className="text-2xl font-bold text-white">
              {gesture.name}
            </h2>

            <p className="text-slate-400 mt-3">
              {gesture.action}
            </p>

          </div>
        ))}

      </div>

    </div>
  );
}