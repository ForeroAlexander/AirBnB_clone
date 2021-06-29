#!/usr/bin/python3
"""comments"""

from models.base_model import BaseModel


class Place(BaseModel):
    """structureof the db"""
    city_id = ""  # city.id format
    user_id = ""  # user.id format
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = ""  # amenity.ids format
