# 🚀 Databricks Jobs Agent

> AI-powered pipeline monitoring assistant for Databricks workloads — built with LangChain and Streamlit.

---

## Overview

Databricks Jobs Agent is an intelligent monitoring tool that connects to your Databricks workspace and provides real-time insights into job run statuses. Powered by an LLM agent, it understands natural language queries and returns structured, markdown-formatted summaries of your running, successful, and failed jobs.

---

## Features

- 🔍 **Natural language querying** — ask about your jobs in plain English
- 📊 **Status filtering** — fetch jobs by `RUNNING`, `SUCCESS`, or `FAILED` state
- ⏱️ **Duration tracking** — job durations auto-converted to minutes
- 🤖 **LLM-powered summaries** — concise, formatted responses via GPT-4o-mini
- 🖥️ **Streamlit UI** — clean, interactive web interface

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Agent Framework | LangChain |
| LLM | GPT-4o-mini |
| API | Databricks Jobs REST API v2.1 |
| Auth | Databricks Personal Access Token |
| Config | Python Dotenv |

---

## Project Structure

```
databricks-jobs-agent/
├── app.py               # Main Streamlit application
├── .env                 # Environment variables (not committed)
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.8+
- A Databricks workspace with an active cluster
- A Databricks Personal Access Token
- An OpenAI API key

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/databricks-jobs-agent.git
cd databricks-jobs-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABRICKS_HOST=https://<your-workspace>.azuredatabricks.net
TOKEN=<your-databricks-personal-access-token>
OPENAI_API_KEY=<your-openai-api-key>
```

> **Note:** Never commit your `.env` file. Add it to `.gitignore`.

### 4. Run the application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Usage

Once the app is running, type a natural language prompt into the text area and click **Run**.

**Example prompts:**

```
Show me all failed jobs from the last run.
```
```
How many jobs are currently running and what are their durations?
```
```
Give me a summary of all successful jobs.
```

The agent will call the Databricks API, filter jobs by status, and return a clean markdown-formatted response.

---

## How It Works

```
User Prompt
    │
    ▼
LangChain Agent (GPT-4o-mini)
    │
    ▼
get_jobs_by_status(status)
    │
    ▼
Databricks REST API  ──►  /api/2.1/jobs/runs/list
    │
    ▼
Filter by lifecycle_state / result_state
    │
    ▼
Formatted Response → Streamlit UI
```

The agent decides which status to query based on the user's prompt, calls the `get_jobs_by_status` tool, and returns a structured summary with job names, statuses, and durations in minutes.

---

## Requirements

```
streamlit
langchain
langchain-openai
requests
python-dotenv
```

Install all at once:

```bash
pip install streamlit langchain langchain-openai requests python-dotenv
```

---

## Environment Variables Reference

| Variable | Description |
|---|---|
| `DATABRICKS_HOST` | Your Databricks workspace URL |
| `TOKEN` | Databricks Personal Access Token |
| `OPENAI_API_KEY` | OpenAI API key for the LLM agent |

---

## Known Limitations

- Currently fetches only the most recent job runs page (no pagination support yet)
- Supports three statuses: `RUNNING`, `SUCCESS`, and `FAILED`
- Requires an active internet connection to the Databricks REST API

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## Author

**Manikantha Baddireddy**
Azure Data Engineer | LangChain & LLM Enthusiast
[LinkedIn](https://linkedin.com) · [GitHub](https://github.com) · baddireddy.manikantha@gmail.com

---

## License

This project is licensed under the [MIT License](LICENSE).
