#!/usr/bin/env python3


"""
A class user that inherits from the
BaseModel created
"""


from base_model import BaseModel
import models


class User(BaseModel):
    """
    Models out a user
    has attributes:
                email: string - empty string
                password: string - empty string
                first_name: string - empty string
                last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
