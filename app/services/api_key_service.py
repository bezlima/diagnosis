import secrets
from sqlalchemy.orm import Session
from ..models.api_key_model import APIKey
from ..schemas.api_key_schema import ApiKeyCreate

def get_all_keys(db: Session, skip: int = 0, limit: int = 100):
    keys = db.query(APIKey).offset(skip).limit(limit).all()
    return keys

def get_key_by_owner(owner: str, db: Session):
    key = db.query(APIKey).filter(APIKey.owner == owner).first()
    return key

def create_api_key(key_config: ApiKeyCreate, db: Session):

    api_key = secrets.token_hex(16)

    key_data = APIKey(
        key = api_key,
        owner = key_config.owner,
        contact = key_config.contact
    )
    
    db.add(key_data)
    db.commit()
    db.refresh(key_data)
    
    return key_data
