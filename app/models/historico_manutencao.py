from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
import enum

class TipoManutencao(enum.Enum):
    PREVENTIVA = "Preventiva"
    CORRETIVA = "Corretiva"

class HistoricoManutencao(SQLModel, table=True):
    __tablename__ = "historicos_manutencao"

    id: int | None = Field(default=None, primary_key=True)

    equipamento_id: int = Field(foreign_key="equipamentos.id")
    tecnico_id: int = Field(foreign_key="tecnicos.id")

    tipo_manutencao: TipoManutencao
    descricao: str

    realizada_em: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    proxima_previsto: datetime | None = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    equipamento: Optional["Equipamento"] = Relationship(back_populates="historicos")

    tecnico: Optional["Tecnico"] = Relationship(back_populates="manutencoes")