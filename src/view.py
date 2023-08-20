import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import numpy as np
import pandas as pd
from Matrix_Calculator import MatrixCalculator


class MatrixCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        self.matrix_input_box = None  # Text widget for matrix input
        self.result_text = tk.StringVar()
        self.rows_entry = None
        self.cols_entry = None
        self.output_text_box = None  # Text widget for displaying output

        self.create_size_input()
        self.create_matrix_input()
        self.create_output_box()
        self.create_buttons()

    def create_size_input(self):
        size_frame = tk.Frame(self.root)
        size_frame.pack()

        rows_label = tk.Label(size_frame, text="Rows:")
        rows_label.pack(side=tk.LEFT)
        self.rows_entry = tk.Entry(size_frame)
        self.rows_entry.pack(side=tk.LEFT)

        cols_label = tk.Label(size_frame, text="Cols:")
        cols_label.pack(side=tk.LEFT)
        self.cols_entry = tk.Entry(size_frame)
        self.cols_entry.pack(side=tk.LEFT)

        size_submit_button = tk.Button(size_frame, text="Submit", command=self.create_matrix_input)
        size_submit_button.pack()

    def create_matrix_input(self):
        if not self.rows_entry.get() or not self.cols_entry.get():
            messagebox.showerror("Error", "Please enter valid values for rows and columns.")
            return

        if self.matrix_input_box:
            self.matrix_input_box.pack_forget()

        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())

        label = tk.Label(self.root, text="Enter Matrix (rows x cols):")
        label.pack()

        self.matrix_input_box = tk.Text(self.root, height=rows, width=cols * 5)  # Adjust width to accommodate numbers
        self.matrix_input_box.pack()


    def create_output_box(self):
        label = tk.Label(self.root, text="Output:")
        label.pack()

        self.output_text_box = tk.Text(self.root, height=5, width=30)
        self.output_text_box.pack()

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        transpose_button = tk.Button(
            button_frame, text="Transpose", command=self.transpose_matrix
        )
        transpose_button.pack(side=tk.LEFT)

        determinant_button = tk.Button(
            button_frame, text="Determinant", command=self.calculate_determinant
        )
        determinant_button.pack(side=tk.LEFT)

        inverse_button = tk.Button(
            button_frame, text="Inverse", command=self.calculate_inverse
        )
        inverse_button.pack(side=tk.LEFT)

    def get_input_matrix(self):
        matrix_text = self.matrix_input_box.get("1.0", "end-1c")
        rows = matrix_text.split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return matrix

    def update_output(self, result):
        self.output_text_box.delete("1.0", "end")
        self.output_text_box.insert("1.0", result)

    def transpose_matrix(self):
        matrix = self.get_input_matrix()
        calculator = MatrixCalculator()
        result = calculator.transpose(matrix)
        self.update_output(result)

    def calculate_determinant(self):
        matrix = self.get_input_matrix()
        calculator = MatrixCalculator()
        result = calculator.determinant(matrix)
        self.update_output(result)

    def calculate_inverse(self):
        matrix = self.get_input_matrix()
        calculator = MatrixCalculator()
        result = calculator.inverse(matrix)
        self.update_output(result)


