from dataclasses import dataclass
from tkinter import IntVar, BooleanVar

@dataclass
class ModifierData:
    """ Class that keeps track of all the things that could affect a die roll """
    number_of_dice:IntVar
    modifier:IntVar
    apply_modifier_to_all:BooleanVar