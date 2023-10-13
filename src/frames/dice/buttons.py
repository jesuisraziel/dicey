import tkinter as tk
from tkinter import ttk, PhotoImage
from data_classes import PositionOptions
from pathlib import Path
from PIL import Image, ImageTk

class DiceButton(ttk.Button):
    def __init__(self,root:ttk.Widget, label:str, options:PositionOptions):
        self.image = ImageTk.PhotoImage(Image.open('assets/125x125.png'))
        

        super().__init__(root, image=self.image, text=label)
        col = options.col
        row = options.row
        self.grid(row=row, column=col)
