from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🧬 Shrine is alive"}

@app.post("/ignite")
async def ignite(request: Request):
    body = await request.json()
    key = body.get("key")
    action = body.get("action")

    if key == "AU-Saad-Patel-Override" and action == "ignite":
        return {"status": "✅ Ignition complete"}
    else:
        return {"status": "❌ Unauthorized"}
