from sqlalchemy.orm import Session
from ..models import report_models
from ..schemas import report_schema

def get_reports(db: Session, skip: int = 0, limit: int = 100):
    reports = db.query(report_models.Report).offset(skip).limit(limit).all()
    return reports

def get_report_by_client_id(db: Session, client_id: int, skip: int = 0, limit: int = 100):
    reports = db.query(report_models.Report).filter(report_models.Report.client_id == client_id).offset(skip).limit(limit).all()
    return reports

def get_report_by_professional_id(db: Session, professional_id: int, skip: int = 0, limit: int = 100):
    reports = db.query(report_models.Report).filter(report_models.Report.professional_id == professional_id).offset(skip).limit(limit).all()
    return reports

def get_report_by_id(db: Session, report_id: int):
    report = db.query(report_models.Report).filter(report_models.Report.report_id == report_id).first()
    return report

def update_report(db: Session, report_id: int, update_infos: report_schema.ReportBase):
    report = db.query(report_models.Report).filter(report_models.Report.report_id == report_id).first()
    if report:
        update_data = update_infos.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(report, key, value)
        db.commit()
        db.refresh(report)
        return True
    return False

def delete_report(db: Session, report_id: int):
    report = db.query(report_models.Report).filter(report_models.Report.report_id == report_id).first()
    if report:
        db.delete(report)
        db.commit()
        return True
    return

def create_report(db: Session, report: report_models.Report):
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

