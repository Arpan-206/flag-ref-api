from pydantic import BaseModel, NaiveDatetime


class VoteBase(BaseModel):
    score: int
    voter_id: str
    flag_id: int


class Vote(VoteBase):
    id: int
    casted_on: NaiveDatetime

    class Config:
        orm_mode = True


class VoteCreate(VoteBase):
    creation_key: str


class FlagBase(BaseModel):
    image_url: str
    creator_slack_id: str


class Flag(FlagBase):
    id: int
    added_on: NaiveDatetime

    votes: list[Vote] = []

    class Config:
        orm_mode = True


class FlagCreate(FlagBase):
    flag_add_key: str


class FlagWitScore(FlagBase):
    id: int
    added_on: NaiveDatetime
    score: int


class VoterBase(BaseModel):
    slack_id: str
    voted_for: int
    

class Voter(VoterBase):
    id: int
    flags: list[Flag] = []
    class Config:
        orm_mode = True


class VoterCreate(VoteBase):
    pass
