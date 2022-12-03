#!/usr/bin/env python3
"""
Contains all the attributes of the city class
"""


from models.base_model import BaseModel



class City(BaseModel):
    """
    Every detail about the city will be contained here
    """
    state_id = ""
    name = ""
