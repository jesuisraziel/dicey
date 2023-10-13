import tkinter as tk
from tkinter import ttk
from data_classes import PositionOptions
from .buttons import DiceButton

class DiceFrame(ttk.Frame):
    def __init__(self, root:ttk.Widget, options:PositionOptions):
        super().__init__(root)
        col = options.col
        row = options.row

        d2 = DiceButton(self, label="d2", options=PositionOptions(row=0, col=0))
        d4 = DiceButton(self, label="d2", options=PositionOptions(row=0, col=1))
        d6 = DiceButton(self, label="d2", options=PositionOptions(row=0, col=2))

        d8 = DiceButton(self, label="d2", options=PositionOptions(row=1, col=0))
        d10 = DiceButton(self, label="d2", options=PositionOptions(row=1, col=1))
        d12 = DiceButton(self, label="d2", options=PositionOptions(row=1, col=2))

        d20 = DiceButton(self, label="d2", options=PositionOptions(row=2, col=0))
        d100 = DiceButton(self, label="d2", options=PositionOptions(row=2, col=1))
        dX = DiceButton(self, label="d2", options=PositionOptions(row=2, col=2))

        self.columnconfigure(index=[0,1,2], pad="12px")
        self.rowconfigure(index=[0,1,2], pad="12px")
        self.grid(column=col, row=row, columnspan=3, rowspan=3)
        