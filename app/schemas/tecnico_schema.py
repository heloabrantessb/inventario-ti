from pydantic import BaseModel
from app.models.tecnico import Tecnico

class TecnicoBase(BaseModel):
    nome: str
    email: str
    especialidades: list[str]

class TecnicoCreate(TecnicoBase):
    def to_model(self) -> Tecnico:
        return Tecnico(**self.model_dump()) 
    

class TecnicoRead(TecnicoBase):
    id: int
    ativo: bool

    class Config:
        from_attributes = True

class TecnicoUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    especialidades: list[str] | None = None
    ativo: bool | None = None