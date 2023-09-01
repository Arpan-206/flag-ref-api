from sqlalchemy import (Column, DateTime, ForeignKey, Integer, SmallInteger,
                        String)
from sqlalchemy.orm import relationship

from flag_ref_api.database import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column("id", Integer, primary_key=True, index=True)
    score = Column("score", SmallInteger)
    voter_id = Column("voter", String, unique=True)
    casted_on = Column("casted_on", DateTime)
    flag_id = Column(Integer, ForeignKey("flags.id"))

    creator = relationship("Flag", back_populates="votes")


class Flag(Base):
    __tablename__ = "flags"

    id = Column("id", Integer, primary_key=True, index=True)
    creator_slack_id = Column("creator_id", String, unique=True)
    image_url = Column("image_url", String)
    added_on = Column("added_on", DateTime)

    votes = relationship("Vote", back_populates="creator")


class Voter(Base):
    __tablename__ = "voters"

    slack_id = Column("slack_id", String, primary_key=True, index=True)
    voted_on = Column("voted_on", DateTime)
