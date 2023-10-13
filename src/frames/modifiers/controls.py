import tkinter as tk
from tkinter import ttk, BooleanVar, IntVar
from tkinter import IntVar
from enum import Enum
from data_classes import PositionOptions, IntegerControlOptions, IntegerControlType

class ControlType(Enum):
    DICE = 1
    MOD = 2

class IntegerControl(ttk.Frame):
    def __init__(self, root:ttk.Widget, label:str, watched_value:IntVar, options:IntegerControlOptions):
        super().__init__(root)
        #Keep a reference to the watched value.
        self.watched = watched_value
        self.type = options.type
        #Set increment, decrement buttons, as well as value label.
        col = options.col
        row = options.row
        self.grid(column=col, row=row)
        
        label = ttk.Label(self, text=label)
        label.grid(column=0, row=0, columnspan=3)

        decrement_btn = ttk.Button(self, text="-", command=self.decrement_value)
        if(self.type is not IntegerControlType.INTEGER):
            decrement_btn.state(['disabled'])
        decrement_btn.grid(column=0, row=1)
        self.decrement_btn = decrement_btn

        label = ttk.Label(self)
        label['textvariable'] = self.watched
        label.grid(column=1, row=1)
        self.label = label

        increment_btn = ttk.Button(self, text="+", command=self.increment_value)
        increment_btn.grid(column=2, row=1)
        self.increment_btn = increment_btn

    def increment_value(self, *args):
        if(self.type is not IntegerControlType.INTEGER and self.decrement_btn.instate(['disabled'])):
            self.decrement_btn.state(['!disabled'])
        value = self.watched.get()
        new_value = value+1
        self.watched.set(new_value)

    def decrement_value(self, *args):
        value = self.watched.get()
        new_value = 1 if (value <= 1 and self.type is not IntegerControlType.INTEGER) else value-1
        if((self.type == IntegerControlType.NONZERO and new_value == 1) or (self.type == IntegerControlType.NATURAL and new_value == 0)):
            self.decrement_btn.state(['disabled'])
        self.watched.set(new_value)

class BooleanControl(ttk.Frame):
    def __init__(self, root:ttk.Widget, watched_value:BooleanVar, label:str, options: PositionOptions):
        super().__init__(root)
        self.watched = watched_value
        checkbox = ttk.Checkbutton(self,variable=self.watched, text=label)
        col = options.col
        row = options.row
        checkbox.grid(column=0, row=0)
        self.grid(column=col, row=row)

