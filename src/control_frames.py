import tkinter as tk
from tkinter import ttk

class ControlsFrame(ttk.Frame):
    def __init__(self, root, dice_data):
        super().__init__(root)
        self.dice_data = dice_data

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid()

        self.setup_modifier_controls()
        self.setup_dice_controls()
        

    def setup_modifier_controls(self):
        
        decrement_button = ttk.Button(self, text="-", command=self.decrement)
        decrement_button.grid(column=0, row=0)
        decrement_button.state(['disabled'])
        self.decrement_button = decrement_button

        label = ttk.Label(self)
        label['textvariable'] = self.dice_data.modifier
        label.grid(column=1, row=0)
        self.label = label

        increment_button = ttk.Button(self, text="+", command=self.increment)
        increment_button.grid(column=2, row=0)
        self.increment_button = increment_button

    def increment(self, *args):
        if(self.decrement_button.instate(['disabled'])):
            self.decrement_button.state(['!disabled'])
        value = self.dice_data.modifier.get()
        new_value = value+1
        self.dice_data.modifier.set(new_value)

    def decrement(self, *args):
        value = self.dice_data.modifier.get()
        new_value = 1 if value <= 1 else value-1
        if(new_value == 1):
            self.decrement_button.state(['disabled'])
        self.dice_data.modifier.set(new_value)