const gestures = [
  {
    emoji: "🖐",
    name: "OPEN PALM",
    action: "Activate Assistant",
    description:
      "Wake up VisionAssist AI and enter active mode.",
    color: "border-green-500",
    glow: "hover:shadow-green-500/30",
    status: "ACTIVE",
  },
  {
    emoji: "☝",
    name: "INDEX",
    action: "Start Listening",
    description:
      "Capture your voice command for processing.",
    color: "border-cyan-500",
    glow: "hover:shadow-cyan-500/30",
    status: "ACTIVE",
  },
  {
    emoji: "👍",
    name: "THUMBS UP",
    action: "Execute Command",
    description:
      "Approve and execute the recognised command.",
    color: "border-blue-500",
    glow: "hover:shadow-blue-500/30",
    status: "ACTIVE",
  },
  {
    emoji: "👎",
    name: "THUMBS DOWN",
    action: "Retry Command",
    description:
      "Reject the command and start listening again.",
    color: "border-yellow-500",
    glow: "hover:shadow-yellow-500/30",
    status: "ACTIVE",
  },
  {
    emoji: "✊",
    name: "FIST",
    action: "Deactivate Assistant",
    description:
      "Stop VisionAssist AI and end the current session.",
    color: "border-red-500",
    glow: "hover:shadow-red-500/30",
    status: "ACTIVE",
  },
  {
    emoji: "✌",
    name: "VICTORY",
    action: "Reserved Feature",
    description:
      "Gesture reserved for upcoming AI capabilities.",
    color: "border-purple-500",
    glow: "hover:shadow-purple-500/30",
    status: "COMING SOON",
  },
];

export default function GestureGuide() {
  return (
    <div className="space-y-10">

      <div className="text-center">

        <h1 className="text-5xl font-bold text-white">
          Gesture Control Centre
        </h1>

        <p className="text-slate-400 mt-4 max-w-3xl mx-auto">
          VisionAssist AI uses intuitive hand gestures to activate,
          control and interact with your personal AI assistant without
          touching the keyboard or mouse.
        </p>

      </div>

      <div className="grid lg:grid-cols-2 xl:grid-cols-3 gap-8">

        {gestures.map((gesture) => (

          <div
            key={gesture.name}
            className={`
              bg-slate-900
              rounded-3xl
              border
              ${gesture.color}
              p-7
              transition-all
              duration-300
              hover:-translate-y-2
              hover:shadow-2xl
              ${gesture.glow}
            `}
          >

            <div className="flex justify-between items-start">

              <div className="text-6xl">
                {gesture.emoji}
              </div>

              <span
                className={`text-xs px-3 py-1 rounded-full font-semibold ${
                  gesture.status === "ACTIVE"
                    ? "bg-green-600 text-white"
                    : "bg-purple-600 text-white"
                }`}
              >
                {gesture.status}
              </span>

            </div>

            <h2 className="text-2xl font-bold text-white mt-6">
              {gesture.name}
            </h2>

            <p className="text-cyan-400 font-medium mt-2">
              {gesture.action}
            </p>

            <p className="text-slate-400 mt-5 leading-7">
              {gesture.description}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}