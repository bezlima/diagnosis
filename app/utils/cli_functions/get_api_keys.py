from ...services.api_key_service import get_all_keys, get_key_by_owner
from app.db.db import SessionLocal

db = SessionLocal()

def get_api_keys():
    keys = get_all_keys(db)
    return keys

def get_key(owner:str):
    key = get_key_by_owner(owner, db)
    return key