from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🧬 Shrine is alive"}

@app.post("/ignite")
def ignite():
    return {"status": "✅ Ignition complete"}
