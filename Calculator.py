import customtkinter as ctk

def update_text(btn):
    text.append(btn)
    label.configure(text=''.join(text))

def ac():
    while(len(text)) > 0:
        text.pop(0)
    label.configure(text='')

def back():
    text.pop(-1)
    label.configure(text=''.join(text))

def evaluate():
    evaluation = eval(''.join(text))
    text.append('=')
    text.append(str(evaluation))
    label.configure(text=''.join(text))

window = ctk.CTk()
window.title('Calculator')
text=[]
label = ctk.CTkLabel(window, width=168, height=60, text='')
label.grid(row=0, columnspan = 4)
btn_list = ['AC', 'back', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', 'p', '0', ',', '=']
actual_buttons = {}
column = 0
row = 1
for btn in btn_list:
    if column % 4 == 0:
        row = row + 1
        column = 0
    if btn not in ['AC', 'back', 'p', '=']:
        button = ctk.CTkButton(window, width=40, height=40, text=btn, command=lambda input_value = btn: update_text(input_value))
    elif btn == 'AC':
        button = ctk.CTkButton(window, width=40, height=40, text=btn, command=ac)
    elif btn == 'back':
        button = ctk.CTkButton(window, width=40, height=40, text=btn, command=back)
    elif btn == 'p':
        button = ctk.CTkButton(window, width=40, height=40, text=btn)
    elif btn == '=':
        button = ctk.CTkButton(window, width=40, height=40, text=btn, command=evaluate)
    button.grid(column= column, row = row, padx= 2, pady = 5)
    actual_buttons[btn] = button
    column = column + 1
window.mainloop()