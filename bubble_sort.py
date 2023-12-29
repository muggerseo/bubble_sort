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

def sort_increase():
    global seq
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    update_result_label()

def sort_decrease():
    global seq
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] < seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    update_result_label()

def set_window_style():
    s = ttk.Style()
    s.configure('TFrame', background='lightgrey')
    s.configure('TLabel', background='lightgrey', foreground='black', font=('Arial', 10, 'bold'))
    s.configure('TButton', background='orange', foreground='black',
                font=('Times new Roman', 10, 'bold'), padding=(10,5))

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinates = (screen_width - width) // 2
    y_coordinates = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinates}+{y_coordinates}")
   
def reset_fields():
    answer = messagebox.askquestion('Reset input field?')
    if answer == 'yes':
        input_1.delete(0, tk.END)
        input_1.focus_set()
        result_label.config(text="")
    elif answer == 'NO':
        messagebox.showinfo("Canselled", "Reset canceled")

# seq = 7 33 73 642 4322 6677 0 1 2 

window = tk.Tk()
window.title("Sort prog")
#window.geometry('250x300')
window_width = 250
window_height = 300
#window.resizable(True,True)
center_window(window, window_width, window_height)

set_window_style()

input_frame = ttk.Frame(window, style='TFrame')
input_frame.grid(pady=10)

label_1 = ttk.Label(input_frame, text="Enter numbers, space separeted: ", style='TLabel')
label_1.grid(row=0, columnspan=2, pady=10, padx=20)
input_1 = tk.Entry(input_frame, bg='white')
input_1.grid(row=1, columnspan=2, sticky='N')
input_1.focus_set()
input_1.bind('<Return>', lambda event: get_input())

input_button = ttk.Button(input_frame, text='Submit', command=get_input, style='TButton')
input_button.grid(row=2, columnspan=2, pady=10)

increase_button = ttk.Button(input_frame, text='Increase', command=sort_increase)
increase_button.grid(row=3, column=0)
increase_button.bind('<Return>', lambda event: sort_increase())

decrese_button = ttk.Button(input_frame, text='Decrease', command=sort_decrease)
decrese_button.grid(row=3, column=1)
decrese_button.bind('<Return>', lambda event: sort_decrease())

result_frame = ttk.Frame(window, style='TFrame')
result_frame.grid(row=5, columnspan=2, pady=10)

result_label = ttk.Label(result_frame, style='TLabel', text="")
result_label.grid(row=6, columnspan=2, pady=20)

reset_button = ttk.Button(input_frame, text='Reset', command=reset_fields)
reset_button.grid(row=7, columnspan=2, pady=20)
reset_button.bind('<Return>', lambda event=NONE:reset_fields())


if __name__ == '__main__':
    window.mainloop()