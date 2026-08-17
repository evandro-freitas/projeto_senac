from fastapi import APIRouter, Depends, HTTPException, status

from app.security import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("")
def admin_area(user=Depends(get_current_user)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticação necessária",
        )

    if user["role"] != "admin":
       
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Acesso não permitido",
        )

    return {
        "message": "Área administrativa",
        "user": user,
    }
