from dataclasses import dataclass
from tkinter import IntVar, BooleanVar
from enum import Enum

@dataclass
class ModifierData:
    """ Class that keeps track of all the things that could affect a die roll """
    number_of_dice:IntVar
    modifier:IntVar
    apply_modifier_to_all:BooleanVar

@dataclass
class PositionOptions:
    """Class that contained information needed to set up a widget's position within a grid."""
    row:int
    col:int

class IntegerControlType(Enum):
    INTEGER = "INTEGER"
    NONZERO = "NONZERO"
    NATURAL = "NATURAL"

@dataclass
class IntegerControlOptions(PositionOptions):
    type:IntegerControlType