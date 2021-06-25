#!/usr/bin/python3
"""comments"""

from models.base_model import BaseModel

class review(BaseModel):
    place_id = "" #place.id format
    user_id = "" #user.id format
    text = ""
