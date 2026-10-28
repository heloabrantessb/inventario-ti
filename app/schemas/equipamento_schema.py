from pydantic import BaseModel
from datetime import datetime
from app.models.equipamento import TipoEquipamento

class EquipamentoCreate(BaseModel):
    nome: str
    tipo: TipoEquipamento
    patrimonio: str
    setor: str
    tecnico_responsavel_id: int
    data_aquisicao: datetime | None = None
    periodicidade_dias: int

class EquipamentoRead(BaseModel):
    id: int
    nome: str
    tipo: TipoEquipamento
    patrimonio: str
    setor: str
    tecnico_responsavel_id: int
    data_aquisicao: datetime | None = None
    ultima_manutencao: datetime  | None = None
    periodicidade_dias: int
    ativo: bool

    class Config:
        from_attributes = True

class EquipamentoUpdate(BaseModel):
    nome: str | None = None
    tipo: TipoEquipamento | None = None
    patrimonio: str | None = None
    setor: str | None = None
    tecnico_responsavel_id: int | None = None
    data_aquisicao: datetime | None = None
    ultima_manutencao: datetime  | None = None
    periodicidade_dias: int | None = None
    ativo: bool | None = None