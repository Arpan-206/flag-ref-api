from datetime import datetime

from sqlalchemy.orm import Session

from flag_ref_api import encrypto, models, schema


def get_vote(db: Session, id: int):
    return db.query(models.Vote).filter(models.Vote.id == id).first()


def get_voter(db: Session, slack_id: str):
    return db.query(models.Voter).filter(models.Voter.slack_id == slack_id).first()


def get_flag(db: Session, id: int):
    return db.query(models.Flag).filter(models.Flag.id == id).first()


def get_flag_by_slack(db: Session, slack_id: str):
    return (
        db.query(models.Flag).filter(models.Flag.creator_slack_id == slack_id).first()
    )


def get_vote_by_slack(db: Session, slack_id: str):
    enc_slack_id = encrypto.encrypt(slack_id)
    return db.query(models.Vote).filter(models.Vote.voter_id == enc_slack_id).first()


def get_votes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vote).offset(skip).limit(limit).all()


def get_flags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Flag).offset(skip).limit(limit).all()


def create_flag(db: Session, flag: schema.FlagCreate):
    db_flag = models.Flag(
        image_url=flag.image_url,
        creator_slack_id=flag.creator_slack_id,
        added_on=datetime.now(),
    )

    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)

    return db_flag


def create_vote(db: Session, vote: schema.VoteCreate, flag_id: int):
    enc_voter_slack = encrypto.encrypt(vote.voter_id)

    if vote.score > 10 or vote.score < 0:
        raise ValueError("Invalid score")

    if get_flag(db, flag_id) is None:
        raise ValueError("Flag ID invalid.")

    db_vote = models.Vote(
        score=vote.score,
        casted_on=datetime.now(),
        voter_id=enc_voter_slack,
        flag_id=flag_id,
    )
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote


def create_voter(db: Session, voter: schema.VoterCreate):
    db_voter = models.Voter(slack_id=voter.slack_id, voted_on=datetime.now())

    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)

    return db_voter
