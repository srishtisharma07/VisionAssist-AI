from app.agents.graph import graph
from app.services.assistant_state import assistant_state


class AgentOrchestrator:

    def execute(self, command: str):

        assistant_state.set_command(command)

        result = graph.invoke(
            {
                "user_input": command,
                "selected_tool": "",
                "response": "",
            }
        )

        assistant_state.set_response(result["response"])

        return {
            "selected_tool": result["selected_tool"],
            "response": result["response"],
        }


agent = AgentOrchestrator()