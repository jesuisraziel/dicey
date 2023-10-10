import tkinter as tk
from tkinter import ttk
from dice_roller import Die
from data_classes import ModifierData
from frames.modifiers.modifier_frame import ModifiersFrame

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

    # Adding components to application frame.
    modifier_frame = ModifiersFrame(root, modifier_data)
    root.mainloop()