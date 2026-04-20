from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from app.models.tecnico import Tecnico
from app.models.equipamento import Equipamento
from app.models.historico_manutencao import HistoricoManutencao

app = FastAPI()

@app.on_event("startup")
def on_startup():
    print("CRIANDO TABELAS...")
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}