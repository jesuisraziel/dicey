import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from enum import Enum

class ControlType(Enum):
    DICE = 1
    MOD = 2

class ValueControl(ttk.Frame):
    def __init__(self, root, label, watched_value, col, row):
        super().__init__(root)
        #Keep a reference to the watched value.
        self.watched = watched_value
        #Set increment, decrement buttons, as well as value label.
        self.grid(column=col, row=row)
        
        label = ttk.Label(self, text=label)
        label.grid(column=0, row=0, columnspan=3)

        decrement_btn = ttk.Button(self, text="-", command=self.decrement_value)
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
        if(self.decrement_btn.instate(['disabled'])):
            self.decrement_btn.state(['!disabled'])
        value = self.watched.get()
        new_value = value+1
        self.watched.set(new_value)

    def decrement_value(self, *args):
        value = self.watched.get()
        new_value = 1 if value <= 1 else value-1
        if(new_value == 1):
            self.decrement_btn.state(['disabled'])
        self.watched.set(new_value)