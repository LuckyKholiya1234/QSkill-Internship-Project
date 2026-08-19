import tkinter as tk
from tkinter import messagebox
import numpy as np


# Function to get matrix from text box
def get_matrix(text):
    try:
        rows = text.strip().split("\n")

        matrix = []

        for row in rows:
            values = row.split(",")
            matrix.append([float(value.strip()) for value in values])

        return np.array(matrix)

    except:
        messagebox.showerror("Error", "Please enter a valid matrix!")
        return None


# Addition
def addition():
    matrix1 = get_matrix(matrix1_text.get("1.0", tk.END))
    matrix2 = get_matrix(matrix2_text.get("1.0", tk.END))

    if matrix1 is not None and matrix2 is not None:
        try:
            result = matrix1 + matrix2
            result_label.config(text="Result:\n" + str(result))

        except ValueError:
            messagebox.showerror(
                "Error",
                "Both matrices must have the same size!"
            )


# Subtraction
def subtraction():
    matrix1 = get_matrix(matrix1_text.get("1.0", tk.END))
    matrix2 = get_matrix(matrix2_text.get("1.0", tk.END))

    if matrix1 is not None and matrix2 is not None:
        try:
            result = matrix1 - matrix2
            result_label.config(text="Result:\n" + str(result))

        except ValueError:
            messagebox.showerror(
                "Error",
                "Both matrices must have the same size!"
            )


# Multiplication
def multiplication():
    matrix1 = get_matrix(matrix1_text.get("1.0", tk.END))
    matrix2 = get_matrix(matrix2_text.get("1.0", tk.END))

    if matrix1 is not None and matrix2 is not None:
        try:
            result = np.dot(matrix1, matrix2)
            result_label.config(text="Result:\n" + str(result))

        except ValueError:
            messagebox.showerror(
                "Error",
                "Matrices cannot be multiplied. Check their dimensions!"
            )


# Transpose of Matrix 1
def transpose_matrix1():
    matrix1 = get_matrix(matrix1_text.get("1.0", tk.END))

    if matrix1 is not None:
        result = matrix1.T
        result_label.config(text="Transpose of Matrix 1:\n" + str(result))


# Transpose of Matrix 2
def transpose_matrix2():
    matrix2 = get_matrix(matrix2_text.get("1.0", tk.END))

    if matrix2 is not None:
        result = matrix2.T
        result_label.config(text="Transpose of Matrix 2:\n" + str(result))


# Determinant of Matrix 1
def determinant_matrix1():
    matrix1 = get_matrix(matrix1_text.get("1.0", tk.END))

    if matrix1 is not None:
        try:
            result = np.linalg.det(matrix1)

            result_label.config(
                text="Determinant of Matrix 1:\n" + str(round(result, 2))
            )

        except:
            messagebox.showerror(
                "Error",
                "Determinant can only be calculated for a square matrix!"
            )


# Determinant of Matrix 2
def determinant_matrix2():
    matrix2 = get_matrix(matrix2_text.get("1.0", tk.END))

    if matrix2 is not None:
        try:
            result = np.linalg.det(matrix2)

            result_label.config(
                text="Determinant of Matrix 2:\n" + str(round(result, 2))
            )

        except:
            messagebox.showerror(
                "Error",
                "Determinant can only be calculated for a square matrix!"
            )


# Clear everything
def clear_all():
    matrix1_text.delete("1.0", tk.END)
    matrix2_text.delete("1.0", tk.END)
    result_label.config(text="Result will appear here")


# Main window
window = tk.Tk()
window.title("Matrix Operations Tool")
window.geometry("750x650")


# Heading
title = tk.Label(
    window,
    text="Matrix Operations Tool",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# Instructions
instruction = tk.Label(
    window,
    text="Enter values separated by commas and rows on new lines",
    font=("Arial", 10)
)

instruction.pack()


# Matrix 1
matrix1_label = tk.Label(
    window,
    text="Matrix 1",
    font=("Arial", 12, "bold")
)

matrix1_label.pack()

matrix1_text = tk.Text(
    window,
    height=5,
    width=40
)

matrix1_text.pack(pady=5)

# Example
matrix1_text.insert(
    tk.END,
    "1,2\n3,4"
)


# Matrix 2
matrix2_label = tk.Label(
    window,
    text="Matrix 2",
    font=("Arial", 12, "bold")
)

matrix2_label.pack()

matrix2_text = tk.Text(
    window,
    height=5,
    width=40
)

matrix2_text.pack(pady=5)

matrix2_text.insert(
    tk.END,
    "5,6\n7,8"
)


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)


add_button = tk.Button(
    button_frame,
    text="Addition",
    width=12,
    command=addition
)

add_button.grid(row=0, column=0, padx=5, pady=5)


subtract_button = tk.Button(
    button_frame,
    text="Subtraction",
    width=12,
    command=subtraction
)

subtract_button.grid(row=0, column=1, padx=5, pady=5)


multiply_button = tk.Button(
    button_frame,
    text="Multiplication",
    width=12,
    command=multiplication
)

multiply_button.grid(row=0, column=2, padx=5, pady=5)


transpose1_button = tk.Button(
    button_frame,
    text="Transpose M1",
    width=12,
    command=transpose_matrix1
)

transpose1_button.grid(row=1, column=0, padx=5, pady=5)


transpose2_button = tk.Button(
    button_frame,
    text="Transpose M2",
    width=12,
    command=transpose_matrix2
)

transpose2_button.grid(row=1, column=1, padx=5, pady=5)


determinant1_button = tk.Button(
    button_frame,
    text="Determinant M1",
    width=12,
    command=determinant_matrix1
)

determinant1_button.grid(row=1, column=2, padx=5, pady=5)


determinant2_button = tk.Button(
    button_frame,
    text="Determinant M2",
    width=12,
    command=determinant_matrix2
)

determinant2_button.grid(row=2, column=0, padx=5, pady=5)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_all
)

clear_button.grid(row=2, column=1, padx=5, pady=5)


# Result
result_label = tk.Label(
    window,
    text="Result will appear here",
    font=("Arial", 13),
    justify="left"
)

result_label.pack(pady=20)


# Start application
window.mainloop()