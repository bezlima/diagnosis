from fastapi import APIRouter, HTTPException, Depends
from ..services import professional_services
from ..schemas.login_schema import LoginRequest, LoginResponse
from ..utils.hash_password import decrypt_password
from ..utils.jwt_management import create_access_token
from sqlalchemy.orm import Session
from datetime import timedelta
from ..db.db_connect import get_db
from sqlalchemy.exc import SQLAlchemyError

login_router = APIRouter(tags=["Login"])

@login_router.post("/login", response_model=LoginResponse)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):

    try:
        db_professional = professional_services.get_professional_by_email(db, email=login_request.email)

        if db_professional is None or not decrypt_password(login_request.password, db_professional.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token_expires = timedelta(minutes=30)

        access_token = create_access_token(data={"sub": db_professional.email, "professinal_id": db_professional.professional_id, "role": db_professional.role_id}, expires_delta=access_token_expires)
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "email": db_professional.email,
            "professional_id": db_professional.professional_id,
            "role_id": db_professional.role_id
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e