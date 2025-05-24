import requests

from fastmcp import FastMCP

mcp = FastMCP("Omni Query Server")

OMNI_WEBHOOK_URL = (
    "http://34.82.151.95/:5678/webhook/06618753-8762-4e89-8f7b-2c9cafdf23a8"
)
DEFAULT_TOPIC = "associate_agent_metrics_hourly"


@mcp.tool()
def query_omni(prompt: str, topic: str = DEFAULT_TOPIC) -> dict:
    """
    Calls the Omni webhook with the user prompt and topic to retrieve SQL results.
    """
    # Format the body based on Omni's requirements
    payload = {"prompt": prompt, "topic": topic}

    try:
        response = requests.post(
            OMNI_WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()  # Send JSON back to the LLM
    except requests.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
