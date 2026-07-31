import { useEffect, useState } from "react";
import {
  MessageSquare,
  User,
  Bot,
  Clock3,
} from "lucide-react";

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
    <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6 transition-colors duration-300">

      {/* Header */}

      <div className="flex items-center justify-between mb-6">

        <div className="flex items-center gap-3">

          <div className="w-10 h-10 rounded-xl bg-[var(--accent-soft)] flex items-center justify-center">
            <MessageSquare
              size={20}
              className="text-[var(--accent)]"
            />
          </div>

          <div>
            <h2 className="text-xl font-bold text-[var(--text-main)]">
              Conversation Timeline
            </h2>

            <p className="text-xs text-[var(--text-muted)] mt-1">
              Recent interactions with VisionAssist
            </p>
          </div>

        </div>

        <div className="flex items-center gap-2 text-[var(--text-muted)] text-sm">

          <Clock3 size={15} />

          <span>
            Live
          </span>

        </div>

      </div>

      {/* Conversation */}

      <div className="space-y-4 max-h-[500px] overflow-y-auto pr-1">

        {conversation.length === 0 ? (

          <div className="flex flex-col items-center justify-center py-20 text-center">

            <div className="w-14 h-14 rounded-2xl bg-[var(--panel-soft)] border border-[var(--border-color)] flex items-center justify-center">
              <MessageSquare
                size={24}
                className="text-[var(--text-muted)]"
              />
            </div>

            <p className="text-[var(--text-muted)] mt-4">
              No conversation yet.
            </p>

            <p className="text-[var(--text-muted)] text-sm mt-1 opacity-70">
              Activate the assistant and speak a command.
            </p>

          </div>

        ) : (

          conversation.map((item, index) => (

            <div
              key={index}
              className="space-y-3"
            >

              {/* User */}

              <div className="flex gap-3">

                <div className="w-9 h-9 rounded-xl bg-[var(--accent-soft)] flex items-center justify-center shrink-0">
                  <User
                    size={17}
                    className="text-[var(--accent)]"
                  />
                </div>

                <div className="flex-1 bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl rounded-tl-md p-4">

                  <p className="text-xs uppercase tracking-wider text-[var(--text-muted)] mb-2">
                    You
                  </p>

                  <p className="text-[var(--text-main)] leading-6">
                    {item.user}
                  </p>

                </div>

              </div>

              {/* Assistant */}

              <div className="flex gap-3">

                <div className="w-9 h-9 rounded-xl bg-[var(--accent)] flex items-center justify-center shrink-0">
                  <Bot
                    size={17}
                    className="text-white"
                  />
                </div>

                <div className="flex-1 border border-[var(--accent)]/30 rounded-2xl rounded-tl-md p-4 bg-[var(--accent-soft)]">

                  <p className="text-xs uppercase tracking-wider text-[var(--accent)] mb-2">
                    VisionAssist
                  </p>

                  <p className="text-[var(--text-main)] leading-6 whitespace-pre-wrap">
                    {item.assistant}
                  </p>

                </div>

              </div>

            </div>

          ))

        )}

      </div>

    </div>
  );
}