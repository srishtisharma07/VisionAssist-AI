import { useState } from "react";
import { sendCommand } from "../services/api";

function ChatPanel() {

    const [command, setCommand] = useState("");

    const [messages, setMessages] = useState([]);

    async function handleSend() {

        if (!command.trim()) return;

        const userMessage = {
            type: "user",
            text: command,
        };

        setMessages(prev => [...prev, userMessage]);

        const currentCommand = command;

        setCommand("");

        const result = await sendCommand(currentCommand);

        const aiMessage = {
            type: "assistant",
            text: result.response,
        };

        setMessages(prev => [...prev, aiMessage]);

    }

    return (

        <div className="bg-slate-800 rounded-xl shadow-lg p-5 h-[420px] flex flex-col">

            <h2 className="text-xl font-semibold text-white mb-4">
                💬 AI Assistant
            </h2>

            <div className="flex-1 overflow-y-auto bg-slate-900 rounded-lg border border-slate-700 p-4">

                {messages.length === 0 && (

                    <div className="text-slate-500">
                        Ask me anything...
                    </div>

                )}

                {messages.map((msg, index) => (

                    <div
                        key={index}
                        className={`mb-4 flex ${msg.type === "user"
                                ? "justify-end"
                                : "justify-start"
                            }`}
                    >

                        <div
                            className={`${msg.type === "user"
                                    ? "bg-blue-600"
                                    : "bg-green-700"
                                } text-white px-4 py-3 rounded-xl max-w-[80%] whitespace-pre-wrap`}
                        >

                            {msg.text}

                        </div>

                    </div>

                ))}

            </div>

            <div className="mt-4 flex gap-3">

                <input
                    type="text"
                    placeholder="Type your command..."
                    value={command}
                    onChange={(e) => setCommand(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            handleSend();
                        }
                    }}
                    className="flex-1 rounded-lg bg-slate-900 border border-slate-700 text-white px-4 py-3 outline-none focus:border-blue-500"
                />

                <button
                    onClick={handleSend}
                    className="bg-blue-600 hover:bg-blue-700 px-6 rounded-lg text-white font-semibold"
                >
                    Send
                </button>

            </div>

        </div>

    );

}

export default ChatPanel;