import WebcamPanel from "../components/WebcamPanel";
import AssistantStatus from "../components/AssistantStatus";
import ChatPanel from "../components/ChatPanel";

export default function Assistant() {
  return (
    <div className="space-y-8">

      {/* Page Header */}

      <section>
        <p className="text-cyan-400 text-sm uppercase tracking-[0.2em]">
          AI Control Centre
        </p>

        <h1 className="text-4xl font-bold text-white mt-2">
          VisionAssist Assistant
        </h1>

        <p className="text-slate-400 mt-3 max-w-2xl">
          Control your computer using hand gestures and voice commands
          while monitoring the assistant in real time.
        </p>
      </section>

      {/* Main Control Area */}

      <section className="grid xl:grid-cols-3 gap-6">

        <div className="xl:col-span-2">
          <WebcamPanel />
        </div>

        <div>
          <AssistantStatus />
        </div>

      </section>

      {/* Conversation */}

      <section>
        <ChatPanel />
      </section>

    </div>
  );
}