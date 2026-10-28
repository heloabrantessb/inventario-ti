from typing import Optional
from sqlmodel import select, Session
from app.models.tecnico import Tecnico
from app.schemas.tecnico_schema import TecnicoUpdate

def criar_tecnico(session: Session, tecnico: Tecnico) -> Tecnico:
    session.add(tecnico)
    session.commit()
    session.refresh(tecnico)
    return tecnico

def listar_tecnicos(session: Session):
    statement = select(Tecnico)
    tecnicos = session.exec(statement).all()
    return tecnicos

def listar_tecnico_por_id(session: Session, tecnico_id: int) -> Optional[Tecnico]:
    tecnico = session.get(Tecnico, tecnico_id)

    if not tecnico:
        return None
    
    return tecnico

def atualizar_tecnico(session: Session, tecnico_id: int, data: TecnicoUpdate) -> Tecnico:
    tecnico = session.query(Tecnico).filter(Tecnico.id == tecnico_id).first()
    if not tecnico:
        return None
    
    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(tecnico, key, value)

    session.commit()
    session.refresh(tecnico)
    return tecnico

def deletar_tecnico(session: Session, tecnico_id: int) -> bool:
    tecnico = session.query(Tecnico).filter(Tecnico.id == tecnico_id).first()

    if not tecnico:
        return False
    
    session.delete(tecnico)
    session.commit()
    return True


