import tkinter as tk

from diffmodel import ready_diff_model
from fullmodel import convert_to_diff

print("Close me")


def make_full_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=convert_to_diff)


def make_diff_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=ready_diff_model)


win = tk.Tk()
win.geometry(f"600x400+100+200")
win.title('xml ready loader')
win.resizable(False, False)

textDiff = "Подготовить diffmodel xml к загрузке на CIM-портал, экспортированный по профилю для организаций."
tk.Label(win, text=textDiff).grid(row=0, column=0, stick='w')

textFull = "Преобразовать fullmodel xml в diffmodel для загрузки на CIM-портал"
tk.Label(win, text=textFull).grid(row=2, column=0, stick='w')

make_diff_button('Выбрать diff').grid(row=1, column=0, padx=5, pady=5)
make_full_button('Выбрать full').grid(row=3, column=0, padx=5, pady=5)

win.mainloop()
