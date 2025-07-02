# 🤖 Job Agent Service

The Job Agent Service is a lightweight AI-based microservice within the **SE4458 Job Search Platform**. It interacts with users via natural language and interprets queries like “Find me frontend jobs in Istanbul.” It then uses internal APIs to fetch and respond with relevant job listings.

---

## 🧠 Overview

- Accepts natural language input from the user (e.g., chatbox).
- Calls appropriate internal REST APIs (e.g., Job Search Service).
- Returns structured responses based on interpreted intent.
- Built with Python and uses Together.ai (or similar) for LLM-based processing.

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Flask** (or FastAPI)
- **Together.ai API** (or similar LLM provider)
- **Requests** (HTTP client)
- **Docker**

---

## 📁 Project Structure

```
4458JobAgent/
├── main.py               # Flask entrypoint with /api/v1/ai/message route
├── agent.py              # Core logic for message processing and API calls
├── requirements.txt      # Python dependencies
└── Dockerfile            # Containerization setup
```

---

## 💡 Example Flow

1. **User Message:**  
   `"Show me full-stack jobs in Ankara."`

2. **Agent Behavior:**
   - Parses intent and keywords using LLM (Together.ai).
   - Calls Job Search API (`/api/v1/jobs/search?title=full-stack&city=Ankara`)
   - Returns summarized response with matching jobs and optional "Apply" suggestions.

3. **Response Example:**
   ```
   🔎 Found 3 full-stack jobs in Ankara:
   - Backend Dev at DevCo (Apply)
   - Full Stack Intern at StartLab (Apply)
   - Node.js Engineer at CodeBase (Apply)
   ```

---

## 🚀 Running Locally

```bash
# Clone & enter project
git clone https://github.com/Sehrank8/4458JobAgent.git
cd 4458JobAgent

# Install Python deps
pip install -r requirements.txt

# Start Flask app
python main.py
```

---

## 🔐 Environment Variables

Set the following before running:

- `TOGETHER_API_KEY` — API key for Together.ai or other LLM
- `JOB_SEARCH_SERVICE_URL` — URL for the job search API
- `ADMIN_TOKEN` — (optional) Token to apply to jobs

Use `.env` or export manually.

---

## 🐳 Docker

**Dockerfile:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

Build and run:
```bash
docker build -t job-agent .
docker run -e TOGETHER_API_KEY=xxx -p 8085:8085 job-agent
```

---

## ✨ Example API Usage

```
POST /api/v1/ai/message
```

**Request Body:**
```json
{
  "message": "I want backend jobs in Izmir"
}
```

**Response:**
```json
{
  "response": "Here are some backend jobs in Izmir:
1. Java Dev at SoftTech
2. Node Dev at NetHouse
Would you like to apply to one of these?"
}
```

---

## 📄 License

Part of SE4458 Final Project 2025 Spring Term.
