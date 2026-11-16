
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("health")
def health():
    return {"status": "ok"}


@app.post("/entradas")
def crear_entrada(id: int):
    pass

@app.get("/entradas/{id}")
def get_entradas(id: int):
    pass

@app.post("/entradas/{codigo}/validar")
def validar_entrada(codigo: int):
    pass

@app.get("/entradas/eventos/{id}/resumen")
def resumen_entrada(id: int):
    pass