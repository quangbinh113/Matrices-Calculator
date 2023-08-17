import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
from Matrix_Calculator import Matrix_Calculator


class MatrixCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        self.matrix_entries = []
        self.result_text = tk.StringVar()

        self.create_matrix_input()
        self.create_buttons()

    def create_matrix_input(self):
        label = tk.Label(self.root, text="Enter Matrix (rows x cols):")
        label.pack()

        rows = 3  # Default number of rows
        cols = 3  # Default number of columns

        self.matrix_entries = [
            [tk.Entry(self.root) for _ in range(cols)] for _ in range(rows)
        ]

        for i in range(rows):
            for j in range(cols):
                self.matrix_entries[i][j].grid(row=i + 1, column=j)

    def create_buttons(self):
        transpose_button = tk.Button(
            self.root, text="Transpose", command=self.transpose_matrix
        )
        transpose_button.pack()

        determinant_button = tk.Button(
            self.root, text="Determinant", command=self.calculate_determinant
        )
        determinant_button.pack()

        inverse_button = tk.Button(
            self.root, text="Inverse", command=self.calculate_inverse
        )
        inverse_button.pack()

        self.result_label = tk.Label(self.root, textvariable=self.result_text)
        self.result_label.pack()

    def get_input_matrix(self):
        return [
            [float(entry.get()) for entry in row] for row in self.matrix_entries
        ]

    def transpose_matrix(self):
        matrix = self.get_input_matrix()
        calculator = Matrix_Calculator(matrix)
        result = calculator.transpose()
        self.result_text.set(result)

    def calculate_determinant(self):
        matrix = self.get_input_matrix()
        calculator = Matrix_Calculator(matrix)
        result = calculator.determinant()
        self.result_text.set(result)

    def calculate_inverse(self):
        matrix = self.get_input_matrix()
        calculator = MatrixCalculator(matrix)
        result = calculator.inverse()
        self.result_text.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorUI(root)
    root.mainloop()
