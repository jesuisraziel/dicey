import tkinter as tk
from tkinter import ttk
from dice_roller import Die
from data_classes import ModifierData, PositionOptions

from frames.modifiers.modifier_frame import ModifiersFrame
from frames.dice.dice_frame import DiceFrame

if(__name__ == "__main__"):
    # Top level window.
    root = tk.Tk()
    root.title("Dicey")

    # Global application state.
    modifier_data = ModifierData(
        number_of_dice=tk.IntVar(root, value=1),
        modifier=tk.IntVar(root, value=0),
        apply_modifier_to_all=tk.BooleanVar(root, False)
    )

    main_frame = tk.Frame(root)
    main_frame.grid(column=0, row=0)
    

    # Adding components to application frame.
    modifier_frame = ModifiersFrame(main_frame, modifier_data, PositionOptions(row=0, col=3))
    dice_frame = DiceFrame(main_frame, options=PositionOptions(row=0, col=0))
    root.mainloop()