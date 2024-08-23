from pydantic import BaseModel

class RoleBase(BaseModel):
    create_role : bool
    edit_role : bool
    delete_role : bool
    get_all_roles : bool
    get_all_users : bool
    edit_all_user : bool
    delete_all_user : bool
    get_all_reports : bool
    edit_all_reports: bool
    delete_all_reports: bool

class Role(RoleBase):
    role_id: int

    class Config:
        orm_mode = True