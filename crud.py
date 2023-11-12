from sqlalchemy.orm import Session

import models
import schemas


def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()


def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()


def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(email=worker.email)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def get_tractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.tractor).offset(skip).limit(limit).all()


def create_worker_tractor(db: Session, tractor: schemas.TractorCreate, worker_id: int):
    db_tractor = models.tractor(**tractor.dict(), owner_id=worker_id)
    db.add(db_tractor)
    db.commit()
    db.refresh(db_tractor)
    return db_tractor

