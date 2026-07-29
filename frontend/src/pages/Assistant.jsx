import WebcamPanel from "../components/WebcamPanel";
import ChatPanel from "../components/ChatPanel";
import AssistantStatus from "../components/AssistantStatus";

function Assistant() {
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

      <div className="grid grid-cols-3 gap-6">

        <div className="space-y-6">

          <WebcamPanel />

          <AssistantStatus />

        </div>

        <div className="col-span-2">

          <ChatPanel />

        </div>

      </div>

    </div>
  );
}

export default Assistant;