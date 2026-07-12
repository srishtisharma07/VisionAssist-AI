import requests


class WebTool:

    def search(self, query: str) -> str:

        try:

            url = "https://api.duckduckgo.com/"

            params = {
                "q": query,
                "format": "json",
                "no_redirect": 1,
                "no_html": 1,
            }

            response = requests.get(
                url,
                params=params,
                timeout=10,
            )

            data = response.json()

            if data.get("AbstractText"):

                return data["AbstractText"]

            related = data.get("RelatedTopics", [])

            if related:

                first = related[0]

                if isinstance(first, dict):

                    return first.get(
                        "Text",
                        "No result found.",
                    )

            return "No relevant web result found."

        except Exception as e:

            return f"Web Search Error: {e}"


web_tool = WebTool()