import tkinter as tk
from about import about
from custommodel import ready_custom_model
from diffmodel import ready_diff_model
from fullmodel import convert_to_diff
from fullmodelGOST import convert_to_diff_special

print(about)


def make_full_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=convert_to_diff)


def make_full_button_gost_special(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=convert_to_diff_special)


def make_diff_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=ready_diff_model)


def make_custom_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=ready_custom_model)


win = tk.Tk()
win.geometry(f"600x400+100+200")
win.title('xml ready loader')
win.resizable(False, False)

textDiff = "Подготовить diffmodel к загрузке на CIM-портал, экспортированный по профилю для организаций"
tk.Label(win, text=textDiff).grid(row=0, column=0, stick='w')

textFull = "Преобразовать fullmodel без специального экспорта в diffmodel для загрузки на CIM-портал"
tk.Label(win, text=textFull).grid(row=2, column=0, stick='w')

textFull = "Преобразовать fullmodel по ГОСТ в diffmodel для загрузки на CIM-портал"
tk.Label(win, text=textFull).grid(row=4, column=0, stick='w')

textCustom = "Задать параметры преобразования в ручную"
tk.Label(win, text=textCustom).grid(row=6, column=0, stick='w')

make_diff_button('Выбрать').grid(row=1, column=0, padx=5, pady=5)
make_full_button('Выбрать').grid(row=3, column=0, padx=5, pady=5)
make_full_button_gost_special('Выбрать').grid(row=5, column=0, padx=5, pady=5)
make_custom_button('Выбрать').grid(row=7, column=0, padx=5, pady=5)

win.mainloop()
