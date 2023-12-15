import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


seq = []

def get_input():
    global seq
    seq = list(map(int, input_1.get().split()))
    update_result_label()

def update_result_label():
    global seq
    result_label.config(text=f"Result: {seq}")
    result_label.grid(row=5, columnspan=2, pady=20)

def bubble_sort_increase():
    global seq
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    update_result_label()

def bubble_sort_decrease():
    global seq
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] < seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    update_result_label()

def set_window_style():
    s = ttk.Style()
    s.configure('My.TFrame', background='#B1C381')

# seq = 7 33 73 642 4322 6677 0 1 2 

window = tk.Tk()
window.title("Sort prog")
window.geometry('250x300')
window.resizable(True,True)

set_window_style()

input_frame = ttk.Frame(window)
input_frame.grid(pady=10)

label_1 = ttk.Label(input_frame, text="Enter numbers, space separeted: ", font=('Helvecia', 10))
label_1.grid(row=0, columnspan=2, pady=10, padx=20)
input_1 = tk.Entry(input_frame, bg='white')
input_1.grid(row=1, columnspan=2)
input_1.focus_set()
input_1.bind('<Return>', lambda event: get_input())

input_button = ttk.Button(input_frame, text='Submit', command=get_input)
input_button.grid(row=2, columnspan=2, pady=10)

sort_increase_button = ttk.Button(input_frame, text='Increase', command=bubble_sort_increase)
sort_increase_button.grid(row=3, column=0, pady=10)

sort_decrese_button = ttk.Button(input_frame, text='Decrease', command=bubble_sort_decrease)
sort_decrese_button.grid(row=3, column=1, pady=10)

result_label = ttk.Label(input_frame, text="")
result_label.grid(row=5, columnspan=2, pady=20)


if __name__ == '__main__':
    window.mainloop()