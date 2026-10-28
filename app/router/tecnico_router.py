from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.services import tecnico_service
from app.schemas.tecnico_schema import TecnicoCreate, TecnicoRead
from database import get_session

router = APIRouter(prefix="/tecnicos", tags=["Tecnicos"])

@router.post("/", response_model=TecnicoRead, status_code=201)
def create(input_tecnico: TecnicoCreate, session: Session = Depends(get_session)):
    return tecnico_service.create_tecnico(session, input_tecnico)

 