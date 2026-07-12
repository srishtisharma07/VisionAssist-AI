import { useEffect, useState } from "react";
import { getAssistantState } from "../services/api";

function AssistantStatus() {

    const [state, setState] = useState({
        active: false,
        last_gesture: "",
        last_command: "",
        last_tool: "",
        last_response: "",
        last_uploaded_pdf: "",
    });

    useEffect(() => {

        async function loadState() {

            const data = await getAssistantState();

            setState(data);
        }

        loadState();

        const interval = setInterval(loadState, 1000);

        return () => clearInterval(interval);

    }, []);

    return (

        <div className="bg-slate-800 rounded-xl shadow-lg p-5">

            <h2 className="text-xl font-semibold text-white mb-5">
                🤖 Assistant Status
            </h2>

            <div className="space-y-4 text-white">

                <div>
                    <span className="font-semibold">
                        Status:
                    </span>{" "}
                    {state.active ? "🟢 Active" : "🔴 Inactive"}
                </div>

                <div>
                    <span className="font-semibold">
                        Gesture:
                    </span>{" "}
                    {state.last_gesture || "-"}
                </div>

                <div>
                    <span className="font-semibold">
                        Planner Tool:
                    </span>{" "}
                    {state.last_tool || "-"}
                </div>

                <div>
                    <span className="font-semibold">
                        Last Command:
                    </span>

                    <div className="mt-1 text-slate-300">
                        {state.last_command || "-"}
                    </div>
                </div>

                <div>
                    <span className="font-semibold">
                        Last Response:
                    </span>

                    <div className="mt-1 text-slate-300 whitespace-pre-wrap">
                        {state.last_response || "-"}
                    </div>
                </div>

                <div>
                    <span className="font-semibold">
                        Uploaded PDF:
                    </span>{" "}
                    {state.last_uploaded_pdf || "-"}
                </div>

            </div>

        </div>

    );

}

export default AssistantStatus;