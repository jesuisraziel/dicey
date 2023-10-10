import tkinter as tk
from tkinter import ttk
from .controls import ValueControl

class ModifiersFrame(ttk.Frame):
    def __init__(self, root, modifier_state_dataclass):
        super().__init__(root)

        #Keep a reference to the dataclass locally, we'll need to pass it later
        self.modifier_state = modifier_state_dataclass
        #Since we're inheriting from ttk.Frame, we want to set up our geometry.
        self['borderwidth'] = 2
        dice_control = ValueControl(self, "Número de dados", modifier_state_dataclass.number_of_dice, 0, 0)
        mod_control = ValueControl(self, "Modificador", modifier_state_dataclass.modifier, 0, 1)
        self.grid(row=0, column=3, rowspan="3")
        
        


