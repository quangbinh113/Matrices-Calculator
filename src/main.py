import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from Matrix_Calculator import MatrixCalculator
from view import MatrixCalculatorUI


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorUI(root)
    root.mainloop()