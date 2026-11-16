from fastapi import FastAPI

from equipo5wm.rutas.entradas import router as entradas_router

app = FastAPI()
app.include_router(entradas_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("health")
def health():
    return {"status": "ok"}
