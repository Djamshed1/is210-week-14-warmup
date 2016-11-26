#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 warmup task 01"""

import pet

class Dog(pet.Pet):
    """Dog class that has Pet subclass"""

    def __init__(self, has_shots=False, **kwargs):
        """Dog class constructor.

        Args:
            has_shots(boolean, optional): defaults to False
            **kwargs(dict): arbitrary arguments dictionary passed from parent
            class.

        Returns:

        Examples:

        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
