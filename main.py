from fastapi import FastAPI, Request
from agent import extract_query_from_llm, search_jobs

app = FastAPI()

@app.post("/api/v1/agent")
async def agent(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    parsed = extract_query_from_llm(user_input)
    if not parsed or "city" not in parsed or "title" not in parsed:
        print(parsed)
        return {"response": "Sorry, I couldn't understand your request."}

    jobs = search_jobs(parsed["city"], parsed["title"])

    if not jobs or not jobs.get("content"):
        return {"response": f"No jobs found for {parsed['title']} in {parsed['city']}."}

    reply = f"Here are some jobs in {parsed['city']} for '{parsed['title']}':\n"
    for job in jobs["content"]:
        reply += f"- {job['title']} – {job['company']} – {job['type']}\n"

    return {"response": reply}
