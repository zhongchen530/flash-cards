from pynamodb.models import Model
from pynamodb.attributes import *
import os
import uuid

ACCESS_KEY_ID = ""
SECRET_KEY = ""


def User(Model):
    class meta:
        table_name = "user_table"
        aws_access_key_id = os.environ.get("ACCESS_KEY_ID",ACCESS_KEY_ID)
        aws_secret_access = os.environ.get("SECRET_KEY",SECRET_KEY)

    user_id = UnicodeAttribute(hash_key=True)


def Card(Model):
    class meta:
        table_name = "card_table"
        aws_access_key_id = os.environ.get("ACCESS_KEY_ID",ACCESS_KEY_ID)
        aws_secret_access = os.environ.get("SECRET_KEY",SECRET_KEY)

    card_id = UnicodeAttribute(hash=True)
    deck_id = UnicodeAttribute()
    card_front = UnicodeAttribute()
    card_back = UnicodeAttribute()
    user_id = UnicodeAttribute()


def Deck(Model):
    class meta:
        table_name = "deck_table"
        aws_access_key_id = os.environ.get("ACCESS_KEY_ID",ACCESS_KEY_ID)
        aws_secret_access = os.environ.get("SECRET_KEY",SECRET_KEY)
    
    deck_id = UnicodeAttribute(hash_key=True)
    deck_name = UnicodeAttribute()
    user_id = UnicodeAttribute()
    size = NumberAttribute()


def get_uuid(table:Model):
    while True:
        unique_id = uuid.uuid1()
        result = table.query(unique_id,limit=1)
        if next(result,None) is None:
            return unique_id

            
