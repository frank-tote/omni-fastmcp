import requests

from fastmcp import FastMCP

mcp = FastMCP("Analytic Agent Server")

ANALYTIC_AGENT_WEBHOOK_URL = (
    "http://34.82.151.95:5678/webhook/fed2373f-0c65-41c5-8e0a-b2bc9b7f6af9/chat"
)


@mcp.tool()
def analytic_agent(prompt: str) -> dict:
    """
    Calls the Analytic Agent webhook with the user prompt. The agent determines the topic and returns the result.
    """
    payload = {"prompt": prompt}
    try:
        response = requests.post(
            ANALYTIC_AGENT_WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=50,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
