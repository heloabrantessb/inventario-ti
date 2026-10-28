from sqlmodel import Session

from app.repositories.tecnico_repository import criar_tecnico
from app.schemas.tecnico_schema import TecnicoCreate

def create_tecnico(session: Session, data: TecnicoCreate):
    tecnico = data.to_model()

    return criar_tecnico(session, tecnico)