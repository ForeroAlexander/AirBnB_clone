#!/usr/bin/python3

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self *args, **Kwargs):
        """Args:
            id: id of instance
        create_at: time of creation
        update_at: time of creation or modification
        """
