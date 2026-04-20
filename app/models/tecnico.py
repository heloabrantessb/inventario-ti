from datetime import datetime, timezone
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON

class Tecnico(SQLModel, table=True):
    __tablename__ = "tecnicos"

    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True, index=True)

    especialidades: List[str] = Field(sa_column=Column(JSON))

    ativo: bool = Field(default=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    equipamentos: List["Equipamento"] = Relationship(back_populates="tecnico_responsavel")

    manutencoes: List["HistoricoManutencao"] = Relationship(back_populates="tecnico")