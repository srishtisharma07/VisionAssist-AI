from app.agents.graph import graph
from app.services.assistant_state import assistant_state
from app.services.assistant_status import AssistantStatus


class AgentOrchestrator:

    def execute(self, command: str):

        assistant_state.set_command(command)

        assistant_state.set_status(
            AssistantStatus.THINKING
        )

        try:

            result = graph.invoke(
                {
                    "user_input": command,
                    "selected_tool": "",
                    "response": assistant_state.get_last_response(),
                }
            )

            assistant_state.set_tool(
                result["selected_tool"]
            )

            assistant_state.set_response(
                result["response"]
            )

            assistant_state.add_conversation(
                user=command,
                assistant=result["response"],
            )

            assistant_state.set_status(
                AssistantStatus.SPEAKING
            )

            return {
                "selected_tool": result["selected_tool"],
                "response": result["response"],
            }

        except Exception as e:

            assistant_state.set_status(
                AssistantStatus.ERROR
            )

            print(f"\nAgent Error:\n{e}\n")

            return {
                "selected_tool": "",
                "response": "Something went wrong while processing your request.",
            }


agent = AgentOrchestrator()
