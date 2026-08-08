from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import create_user, get_user_by_email
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def register_user(
    name: str,
    email: str,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        return {"message": "User already exists"}

    user = create_user(db, name, email)

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }
