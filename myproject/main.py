from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI(debug=True)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/workers/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    db_workermail = crud.get_worker_by_email(db, email=worker.email)
    if db_workermail:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_worker(db=db, worker=worker)


@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers


@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="worker not found")
    return db_worker


@app.post("/workers/{worker_id}/tractors/", response_model=schemas.Tractor)
def create_tractor_for_worker(
    worker_id: int, tractor: schemas.TractorCreate, db: Session = Depends(get_db)
):
    return crud.create_worker_tractor(db=db, tractor=tractor, worker_id=worker_id)


@app.get("/tractors/", response_model=list[schemas.Tractor])
def read_tractors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tractors = crud.get_tractors(db, skip=skip, limit=limit)
    return tractors


@app.delete("/workers/{worker_id}", response_model=schemas.Worker)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    # Check if the worker exists
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")

    # Delete the worker
    db.delete(db_worker)
    db.commit()

    return db_worker
