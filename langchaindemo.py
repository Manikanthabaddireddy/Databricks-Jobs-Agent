import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
import streamlit as st

load_dotenv()

DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
TOKEN = os.getenv("TOKEN")


def get_jobs_by_status(status: str):
    """Fetch Databricks job runs filtered by status."""

    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/list"

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }


    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return {
            "error": response.text
        }

    data = response.json()
    print(data)

    filtered_jobs = []

    for run in data.get("runs", []):

        state = run.get("state", {})

        result_state = state.get("result_state")
        life_cycle_state = state.get("life_cycle_state")

        is_match = False

        if status.upper() == "RUNNING":
            is_match = life_cycle_state == "RUNNING"
        else:
            is_match = result_state == status.upper()

        if is_match:

            duration_ms = run.get("run_duration", 0)

            filtered_jobs.append({
                "job_name": run.get("run_name"),
                "status": status.upper(),
                "duration_minutes": round(duration_ms / 60000, 2)
            })

    return {
        "count": len(filtered_jobs),
        "jobs": filtered_jobs
    }


pipeline_agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_jobs_by_status],
    system_prompt="""
You are an AI Databricks Monitoring Assistant.

Rules:
1. Durations are already converted into minutes.
2. Clearly separate successful, failed, and running jobs.
3. Provide concise summaries.
4. Use markdown formatting.
"""
)

st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:55px;
    font-weight:800;
    background: linear-gradient(to right, #FF6B00, #FFB347);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Segoe UI';
    margin-bottom: 10px;
}

.subtitle {
    text-align:center;
    font-size:20px;
    color:gray;
    margin-top:-15px;
}
</style>

<div class="main-title">
🚀 Databricks Jobs Agent
</div>

<div class="subtitle">
AI Powered Pipeline Monitoring Assistant
</div>
""", unsafe_allow_html=True)

user_input = st.text_area("Enter Prompt:",height=200)

if st.button("Run"):

    result = pipeline_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    st.write(result["messages"][-1].content)