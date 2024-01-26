#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ['some knowledge']  # Initializing with a list containing at least one element

    def teach(self):
        if not self.knowledge:
            return None
        return self.knowledge[0]