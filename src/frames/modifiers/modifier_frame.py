import tkinter as tk
from tkinter import ttk
from .controls import IntegerControl, BooleanControl
from data_classes import ModifierData, PositionOptions, IntegerControlOptions, IntegerControlType

class ModifiersFrame(ttk.Frame):
    def __init__(self, root, modifier_state_dataclass:ModifierData, options:PositionOptions):
        super().__init__(root)

        #Keep a reference to the dataclass locally, we'll need to pass it later
        self.modifier_state = modifier_state_dataclass
        #Since we're inheriting from ttk.Frame, we want to set up our geometry.
        self['borderwidth'] = 2
        dice_control = IntegerControl(self, "Número de dados", modifier_state_dataclass.number_of_dice, IntegerControlOptions(col=0, row=0, type=IntegerControlType.NONZERO))
        bonus_control = IntegerControl(self, "Modificador", modifier_state_dataclass.modifier, IntegerControlOptions(col=0, row=1,type=IntegerControlType.INTEGER))
        sum_control = BooleanControl(self, modifier_state_dataclass.apply_modifier_to_all, "Aplicar bonificación a cada dado", PositionOptions(col=0, row=2))
        col = options.col
        row = options.row
        self.grid(column=col, row=row, rowspan=3)
        
        


