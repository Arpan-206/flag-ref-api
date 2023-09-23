from flag_ref_api.main import get_db
from flag_ref_api.crud import create_flag
from flag_ref_api.schema import FlagCreate
import os

db = get_db()

db = next(db)

my_dicts = [
    {
        "image_url": "https://cloud-6fxen4pq2-hack-club-bot.vercel.app/0solid_orph.png",
        "creator_slack_id": "U03CBNJUWJG",
    },
    {
        "image_url": "https://cloud-7jdjhy3v4-hack-club-bot.vercel.app/0flag2.png",
        "creator_slack_id": "U05JKJY7A3A",
    },
    {
        "image_url": "https://cloud-c6i119jc7-hack-club-bot.vercel.app/0hc_flag__3_.png",
        "creator_slack_id": "U04LNE9HEFK",
    },
    {
        "image_url": "https://cloud-kuer2ppbs-hack-club-bot.vercel.app/0hcflag6-06-06.png",
        "creator_slack_id": "U04EQJ4RRHA",
    },
    {
        "image_url": "https://cloud-k7xkcv0lb-hack-club-bot.vercel.app/0shiporch2.png",
        "creator_slack_id": "U04KEK4TS72",
    },
    {
        "image_url": "https://cloud-1xqzyjl5q-hack-club-bot.vercel.app/0image.png",
        "creator_slack_id": "U053DV31ATD",
    },
    {
        "image_url": "https://cloud-40mz0w1zg-hack-club-bot.vercel.app/0frame_1_10_.png",
        "creator_slack_id": "U0162MDUP7C",
    }

]

for my_dict in my_dicts:
    print(my_dict)
    flag = FlagCreate(**my_dict, flag_add_key=os.getenv("FLAG_ADD_KEY"))
    create_flag(db,flag)