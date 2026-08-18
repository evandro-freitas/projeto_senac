from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/contact", tags=["Contact"])


class ContactSchema(BaseModel):
    name: str
    email: str
    message: str


@router.post("")
def send_contact(contact: ContactSchema):
    if (
        not contact.name.strip()
        or not contact.email.strip()
        or not contact.message.strip()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Campos obrigatórios não podem estar vazios",
        )

    return {
        "message": "Contato enviado com sucesso!!!"
    }