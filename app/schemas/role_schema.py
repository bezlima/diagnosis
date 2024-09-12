from pydantic import BaseModel

class RoleBase(BaseModel):
    role_name : str

    create_role : bool
    get_your_role : bool
    get_all_roles : bool
    edit_role : bool
    delete_role : bool

    create_professional : bool
    get_all_professionals : bool
    edit_professional : bool
    delete_professional : bool

    create_report : bool
    get_your_report : bool
    get_all_reports : bool
    edit_report: bool
    delete_report: bool

    create_client : bool
    get_your_client : bool
    get_all_clients : bool
    edit_client : bool
    delete_client : bool

    create_pdf: bool

class Role(RoleBase):
    role_id: int

    class Config:
        from_attributes = True