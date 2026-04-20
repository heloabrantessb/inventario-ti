from datetime import datetime, timezone
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
import enum

class TipoEquipamento(enum.Enum):
    DESKTOP = "Desktop"
    NOTEBOOK = "Notebook"
    IMPRESSORA = "Impressora"
    ROTEADOR = "Roteador"
    SWITCH = "Switch"
    SERVIDOR = "Servidor"
    OUTRO = "Outro"

class StatusEquipamento(enum.Enum):
    ATIVO = "Ativo"
    EM_MANUTENCAO = "Em Manutenção"
    DESATIVADO = "Desativado"

class Equipamento(SQLModel, table=True):
    __tablename__ = "equipamentos"

    id: int | None = Field(default=None, primary_key=True)

    nome: str
    tipo: TipoEquipamento
    patrimonio: str = Field(unique=True, index=True)
    setor: str

    tecnico_responsavel_id: int = Field(foreign_key="tecnicos.id")
    tecnico_responsavel: Optional["Tecnico"] = Relationship(back_populates="equipamentos")

    data_aquisicao: datetime | None = None
    ultima_manutencao: datetime | None = None
    periodicidade_dias: int

    status: StatusEquipamento = Field(default=StatusEquipamento.ATIVO)
    ativo: bool = Field(default=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    historicos: List["HistoricoManutencao"] = Relationship(back_populates="equipamento")