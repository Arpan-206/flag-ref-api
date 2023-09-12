from flag_ref_api.crud import clear_flags, clear_votes, clear_voters
from flag_ref_api.main import get_db

# Just a script to clear the database

db = get_db()

db = next(db)

# Order matters here

clear_votes(db)
clear_voters(db)
clear_flags(db)
