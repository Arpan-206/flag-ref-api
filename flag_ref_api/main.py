from datetime import datetime

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from flag_ref_api import crud, models, schema
from flag_ref_api.database import SessionLocal, engine

from flag_ref_api import encrypto

load_dotenv()

import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"Welcome to the Hack Club Naval Armada!"}


@app.post("/cast_vote")
def cast_vote(vote: schema.VoteCreate, db: Session = Depends(get_db)):
    if vote.creation_key != os.getenv("CREATION_KEY"):
        raise HTTPException(401, detail="Creation Key must be valid!")

    try:
        votee = crud.create_vote(db, vote=vote, flag_id=vote.flag_id)
        voter = models.Voter(slack_id=vote.voter_id, voted_on=datetime.now())
        voter_db = (
            db.query(models.Voter)
            .filter(models.Voter.slack_id == voter.slack_id)
            .first()
        )
        if not voter_db:
            voter_db = crud.create_voter(db, voter=voter)
        return votee
    except ValueError:
        raise HTTPException(400, detail="Some of the request parameters are unusual.")


@app.post("/add_flag")
def add_flag(flag: schema.FlagCreate, db: Session = Depends(get_db)):
    if flag.flag_add_key != os.getenv("FLAG_ADD_KEY"):
        raise HTTPException(401, detail="Flag adding key must be valid!")

    if crud.get_flag_by_slack(db, flag.creator_slack_id):
        raise HTTPException(
            status_code=400, detail="A flag from this slack ID already made!"
        )

    try:
        flag = crud.create_flag(db, flag=flag)
        return flag

    except ValueError:
        raise HTTPException(400, detail="Some of the request parameters are unusual.")


@app.get("/get_votes_by_flag")
def get_votes_by_flag(flag_id: int, db: Session = Depends(get_db)):
    flag = crud.get_flag(db, flag_id)

    votes = db.query(models.Vote).filter(models.Vote.flag_id == flag_id).all()

    score = 0

    for i in votes:
        score += i.score

    if flag is None:
        raise HTTPException(404, "Flag not found!")

    flag = schema.FlagWitScore(
        image_url=flag.image_url,
        id=flag.id,
        creator_slack_id=flag.creator_slack_id,
        added_on=flag.added_on,
        score=score,
    )

    return flag


@app.get("/votes")
def votes(db: Session = Depends(get_db)):
    flags = []

    for flag in crud.get_flags(db):
        flag_obj = get_votes_by_flag(flag_id=flag.id, db=db)
        flags.append(flag_obj)

    if len(flags) <= 0:
        raise HTTPException(404, "No votes found")

    return flags


@app.get("/flags")
def flags(db: Session = Depends(get_db)):
    flags = crud.get_flags(db)

    if len(flags) <= 0:
        raise HTTPException(404, "No flags found")

    return flags
