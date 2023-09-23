from flag_ref_api.crud import *
from flag_ref_api.main import get_db

# Just a script to clear the database

db = get_db()

db = next(db)

# Order matters here

clear_votes(db)
clear_voters(db)
# clear_flags(db)

# flag_creator = "U0162MDUP7C"

# flag = get_flag_by_slack(db, flag_creator)

# # Delete the flag

# db.delete(flag)

# db.commit()