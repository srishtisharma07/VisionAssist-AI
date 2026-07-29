import { useEffect, useState } from "react";
import { getAssistantState } from "../services/api";

export default function ChatPanel() {

  const [conversation, setConversation] = useState([]);

  useEffect(() => {

    async function loadConversation() {

      const data = await getAssistantState();

      setConversation(data.conversation || []);

    }

    loadConversation();

    const interval = setInterval(loadConversation, 1000);

    return () => clearInterval(interval);

  }, []);

  return (

    <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

      <h2 className="text-2xl font-bold text-white mb-6">
        Conversation Timeline
      </h2>

      <div className="space-y-4 max-h-[450px] overflow-y-auto">

        {conversation.length === 0 && (

          <div className="text-slate-500 text-center py-20">
            No conversation yet...
          </div>

        )}

        {conversation.map((item, index) => (

          <div
            key={index}
            className="bg-slate-800 rounded-2xl p-4 border border-slate-700"
          >

            <div className="text-cyan-400 font-semibold mb-2">
              👤 {item.user}
            </div>

            <div className="text-white whitespace-pre-wrap">
              🤖 {item.assistant}
            </div>

          </div>

        ))}

      </div>

    </div>

  );

}