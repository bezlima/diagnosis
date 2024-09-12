from fastapi import HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..models.api_key_model import APIKey

API_KEY_NAME = "X-API-Key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key_header: str = Security(api_key_header), db: Session = Depends(get_db)):
    if not api_key_header:
        raise HTTPException(
            status_code=403,
            detail="API Key is missing"
        )
    
    api_key = db.query(APIKey).filter(APIKey.key == api_key_header).first()
    if api_key is None:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    
    return api_key