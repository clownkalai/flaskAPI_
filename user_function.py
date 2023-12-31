from passlib.context import CryptContext
from typing import Union
from datetime import datetime, timedelta

from dbfunctions import *
from flask import abort



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def authenticate_user(username: str, password: str):
    user = find_one_in_collection("userInfo",{"email":username})
    if not user:
        return False
    if not verify_password(password, user[0]["password"]):
        return False
    return user

def getUserByEmailId(email :str):
    user = find_and_filter("userInfo",{"email":email},{"_id":0,"password":0})
    return user

def gentemplateId():
    lasttemp = find_latest_in_collection_sort('templates',[("_id",-1)])
    if lasttemp != []:
        if lasttemp[0]['templateId'] >0:
            tempid = int(lasttemp[0]['templateId'])+1

    else:
        tempid = 1
    return tempid
