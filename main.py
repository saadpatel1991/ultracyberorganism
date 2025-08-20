from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IgniteRequest(BaseModel):
    key: str
    action: str

@app.get("/")
def read_root():
    return {"message": "🧬 Shrine is alive"}

@app.post("/ignite")
def ignite(req: IgniteRequest):
    if req.key == "AU-Saad-Patel-Override" and req.action == "ignite":
        return {"status": "✅ Ignition complete"}
    else:
        return {"status": "❌ Unauthorized"}
