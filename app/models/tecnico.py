import enum
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import JSON

class Tecnico(SQLModel, table=True):
    __tablename__ = "tecnicos"

    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True)
    especialidades: list[str] = Field(sa_column=Column(JSON))
    ativo: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    manutencoes: list["HistoricoManutencao"] = Relationship(back_populates="tecnico")