#!/usr/bin/env python3
"""
All the database modeling for the review class will be stored here
"""



from base_model import BaseModel



class Review(BaseModel):
    """
    Reviews will be modelled out from this class
    """
    place_id = ""
    user_id = ""
    text = ""
