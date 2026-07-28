import { useEffect, useState } from "react";
import { getAssistantState } from "../services/api";

function ConversationHistory() {

    const [history, setHistory] = useState([]);

    useEffect(() => {

        async function loadHistory() {

            try {

                const data = await getAssistantState();

                setHistory(data.conversation || []);

            } catch (err) {

                console.log(err);

            }

        }

        loadHistory();

        const interval = setInterval(loadHistory, 500);

        return () => clearInterval(interval);

    }, []);

    return (

        <div className="bg-slate-800 rounded-xl shadow-lg p-5 h-[450px] flex flex-col">

            <h2 className="text-xl font-semibold text-white mb-4">
                📜 Conversation History
            </h2>

            <div className="flex-1 overflow-y-auto bg-slate-900 rounded-lg border border-slate-700 p-4">

                {history.length === 0 && (

                    <p className="text-slate-500">
                        No conversations yet.
                    </p>

                )}

                {history.map((chat, index) => (

                    <div
                        key={index}
                        className="mb-5 border-b border-slate-700 pb-3"
                    >

                        <p className="text-blue-400 font-semibold">
                            👤 You
                        </p>

                        <p className="text-white mb-3 whitespace-pre-wrap">
                            {chat.user}
                        </p>

                        <p className="text-green-400 font-semibold">
                            🤖 VisionAssist
                        </p>

                        <p className="text-slate-300 whitespace-pre-wrap">
                            {chat.assistant}
                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default ConversationHistory;