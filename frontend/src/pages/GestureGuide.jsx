const gestures = [
  {
    emoji: "🖐",
    name: "OPEN PALM",
    action: "Activate Assistant",
    description:
      "Wake VisionAssist AI and enter the active control mode.",
    status: "ACTIVE",
  },
  {
    emoji: "☝",
    name: "INDEX",
    action: "Start Listening",
    description:
      "Tell the assistant to listen for your voice command.",
    status: "ACTIVE",
  },
  {
    emoji: "👍",
    name: "THUMBS UP",
    action: "Confirm Command",
    description:
      "Approve the recognised command and allow the agent to execute it.",
    status: "ACTIVE",
  },
  {
    emoji: "👎",
    name: "THUMBS DOWN",
    action: "Retry Command",
    description:
      "Reject the current command and ask the assistant to listen again.",
    status: "ACTIVE",
  },
  {
    emoji: "✊",
    name: "FIST",
    action: "Deactivate Assistant",
    description:
      "End the active assistant session and return to the inactive state.",
    status: "ACTIVE",
  },
  {
    emoji: "✌",
    name: "VICTORY",
    action: "Reserved Feature",
    description:
      "Reserved for a future VisionAssist interaction.",
    status: "COMING SOON",
  },
];

export default function GestureGuide() {
  return (
    <div className="space-y-10">

      <section>
        <p className="page-eyebrow">
          Gesture Interface
        </p>

        <h1 className="page-title">
          Gesture Control Centre
        </h1>

        <p className="page-description">
          Learn how each hand gesture interacts with VisionAssist AI.
          Use these gestures to activate, control and deactivate the
          assistant without touching your computer.
        </p>
      </section>

      <section className="grid md:grid-cols-2 xl:grid-cols-3 gap-5">

        {gestures.map((gesture) => (
          <div
            key={gesture.name}
            className="
              group
              bg-[var(--panel-bg)]
              border
              border-[var(--border-color)]
              rounded-3xl
              p-6
              transition-all
              duration-300
              hover:-translate-y-1
              hover:border-[var(--accent)]
            "
          >

            <div className="flex items-start justify-between gap-4">

              <div className="w-16 h-16 rounded-2xl bg-[var(--accent-soft)] border border-[var(--accent)]/20 flex items-center justify-center text-4xl transition-transform duration-300 group-hover:scale-105">
                {gesture.emoji}
              </div>

              <span
                className={`text-[10px] font-bold tracking-wider px-3 py-1.5 rounded-full ${
                  gesture.status === "ACTIVE"
                    ? "bg-[var(--accent-soft)] text-[var(--accent)]"
                    : "bg-[var(--panel-soft)] text-[var(--text-muted)]"
                }`}
              >
                {gesture.status}
              </span>

            </div>

            <h2 className="text-xl font-bold text-[var(--text-main)] mt-6">
              {gesture.name}
            </h2>

            <p className="text-[var(--accent)] font-semibold text-sm mt-2">
              {gesture.action}
            </p>

            <p className="text-sm leading-6 text-[var(--text-muted)] mt-4">
              {gesture.description}
            </p>

          </div>
        ))}

      </section>

      <section className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-7">

        <p className="page-eyebrow">
          Interaction Flow
        </p>

        <h2 className="text-2xl font-bold text-[var(--text-main)] mt-1">
          How to control VisionAssist
        </h2>

        <div className="grid md:grid-cols-3 gap-4 mt-6">

          <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-5">
            <p className="text-[var(--accent)] font-bold">
              01
            </p>

            <h3 className="text-[var(--text-main)] font-semibold mt-3">
              Activate
            </h3>

            <p className="text-sm text-[var(--text-muted)] mt-2 leading-6">
              Show an open palm to activate the assistant.
            </p>
          </div>

          <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-5">
            <p className="text-[var(--accent)] font-bold">
              02
            </p>

            <h3 className="text-[var(--text-main)] font-semibold mt-3">
              Speak
            </h3>

            <p className="text-sm text-[var(--text-muted)] mt-2 leading-6">
              Show your index finger and give a natural voice command.
            </p>
          </div>

          <div className="bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-5">
            <p className="text-[var(--accent)] font-bold">
              03
            </p>

            <h3 className="text-[var(--text-main)] font-semibold mt-3">
              Confirm
            </h3>

            <p className="text-sm text-[var(--text-muted)] mt-2 leading-6">
              Use thumbs up to execute or thumbs down to retry.
            </p>
          </div>

        </div>

      </section>

    </div>
  );
}