from fastapi import APIRouter, status

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_contact(payload: dict):

    name = payload.get("name").strip()
    email = payload.get("email").strip()
    message = payload.get("message").strip()

    if not name or not email or not message:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome, e-mail e mensagem são obrigatórios"
        )

    name = name.strip()
    email = email.strip()           
    message = message.strip()
       
    return {
        "message": "Contato recebido",
        "data": {
            "name": name,
            "email": email,
            "message": message
        },
    }