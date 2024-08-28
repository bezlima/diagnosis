from pydantic import BaseModel

class RoleBase(BaseModel):
    role_name : str

    create_role : bool
    edit_role : bool
    delete_role : bool
    get_all_roles : bool

    create_professionals : bool
    get_all_professionals : bool
    edit_all_professional : bool
    delete_all_professional : bool

    create_report : bool
    get_all_reports : bool
    edit_all_reports: bool
    delete_all_reports: bool

    create_clients : bool
    get_all_clients : bool
    edit_all_client : bool
    delete_all_client : bool

class Role(RoleBase):
    role_id: int

    class Config:
        from_attributes = True