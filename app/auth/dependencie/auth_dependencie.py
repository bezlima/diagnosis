from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...utils.jwt_management import verify_token
from ...services.professional_services import get_professional_by_email
from ...db.db_connect import get_db

def get_current_user(token: str , db: Session = Depends(get_db)):

    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    email = payload.get("email")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = get_professional_by_email(db, email=email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    compare_id = payload.get("professional_id")
    if compare_id != user.professional_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

    compare_role = payload.get("role")
    if compare_role != user.role_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
    
    return user
