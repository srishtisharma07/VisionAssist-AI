import WebcamPanel from "../components/WebcamPanel";
import AssistantStatus from "../components/AssistantStatus";
import ChatPanel from "../components/ChatPanel";

export default function Assistant() {
  return (
    <div className="space-y-6">

      <div>
        <h1 className="text-4xl font-bold text-white">
          AI Assistant
        </h1>

        <p className="text-slate-400 mt-2">
          Control your computer using gestures and voice.
        </p>
      </div>

      <div className="grid lg:grid-cols-3 gap-6">

        <div className="lg:col-span-2">
          <WebcamPanel />
        </div>

        <AssistantStatus />

      </div>

      <ChatPanel />

    </div>
  );
}