from flag_ref_api.crud import *
from flag_ref_api.main import get_db

# Make a script to view all voters

db = get_db()

db = next(db)

voters = get_voters(db)

for voter in voters:
    print(voter.slack_id)

# Make a script to view all flags
