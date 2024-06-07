import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import re

from fullmodel import start_change_fullmodel

print("Close me")

filtered_lines = []
updated_lines = []


def remove_lines(input_file, patterns):
    global filtered_lines
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result = []
    for line in lines:
        # Удаляем 'me:className' и все после него, сохраняя начальные пробелы
        line = re.sub(r'(me:className="[^"]*")', '', line)
        result.append(line)

    filtered_lines = []
    for line in result:
        stripped_line = line.strip()
        remove_line = False
        for start_char, end_char in patterns:
            if stripped_line.startswith(start_char) and stripped_line.endswith(end_char):
                remove_line = True
                break
        if not remove_line:
            filtered_lines.append(line)


def update_lines(old_string1, new_string1, old_string2, new_string2):
    global updated_lines
    updated_lines = [
        new_string1 if line == old_string1 else
        new_string2 if line == old_string2 else
        line
        for line in filtered_lines
    ]


def add_and_save_lines(output_file, add_string, index, add_string2, index2, add_string3, index3):
    global updated_lines
    updated_lines.insert(index, add_string + '\n')
    updated_lines.insert(index2, add_string2 + '\n')
    updated_lines.insert(index3, add_string3 + '\n')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)


def select_file(default_patterns, old_string1, new_string1, old_string2, new_string2, add_string, index, add_string2,
                index2, add_string3, index3):
    input_file = filedialog.askopenfilename(title="Выберите входной файл")
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
                                                   filetypes=[("Text files", "*.xml")])
        if output_file:
            use_defaults = messagebox.askyesno("Использовать значения по умолчанию?",
                                               "Хотите использовать кортежи символов для удаления по умолчанию?")
            if use_defaults:
                patterns = default_patterns
            else:
                patterns = []
                while True:
                    start_char = simpledialog.askstring("Ввод",
                                                        "Введите начальный символ (или оставьте пустым для завершения):")
                    if not start_char:
                        break
                    end_char = simpledialog.askstring("Ввод",
                                                      "Введите конечный символ (или оставьте пустым для завершения):")
                    if not end_char:
                        break
                    patterns.append((start_char, end_char))
            if patterns:
                remove_lines(input_file, patterns)
                update_lines(old_string1, new_string1, old_string2, new_string2)
                add_and_save_lines(output_file, add_string, index, add_string2, index2, add_string3, index3)
                messagebox.showinfo("Готово", "Строки успешно удалены/обновлены и файл сохранен.")
            else:
                messagebox.showwarning("Предупреждение", "Не были заданы пары символов для удаления строк.")


def ready_diff_model():
    # Значения по умолчанию для удаления
    default_patterns = [
        ('<?iec61970-552', '?>'),
        ('<?floatExporter', '?>'),
        ('<rdf:RDF xmlns:', '>'),
        ('<dm:DifferenceModel', '>'),
        ('<md:Model.created>', '>'),
        ('<md:Model.description>', '>'),
        ('<md:Model.version>', '>'),
        ('<me:Model.name>', '>'),
        ('<dm:forwardDifferences', '>'),
        ('<me:', '>')
    ]
    # Значения по умолчанию для замены
    old_string1 = '    <dm:reverseDifferences>\n'
    new_string1 = '    <dm:reverseDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">\n'
    old_string2 = '\ufeff<?xml version="1.0" encoding="utf-8"?>\n'
    new_string2 = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n'

    add_string = '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:so="http://so-ups.ru/2015/schema-cim16#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:dm="http://iec.ch/TC57/61970-552/DifferenceModel/1#" xmlns:rf="http://gost.ru/2019/schema-cim01#" xmlns:ups="https://cim.so-ups.ru#" xml:base="">'
    index = 1

    add_string2 = '  <dm:DifferenceModel>'
    index2 = 2

    add_string3 = '  <dm:forwardDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">'
    index3 = 3

    # Вызов основного метода
    select_file(default_patterns, old_string1, new_string1, old_string2, new_string2, add_string, index, add_string2,
                index2, add_string3, index3)


def ready_full_model():
    messagebox.showinfo("Ошибка", "Раздел в разработке")


def make_diff_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=ready_diff_model)


def make_full_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='black', command=start_change_fullmodel)


win = tk.Tk()
win.geometry(f"600x400+100+200")
win.title('xml ready loader')
win.resizable(False, False)

textDiff = "Подготовить diffmodel xml к загрузке на CIM-портал, экспортированный по профилю для организаций."
tk.Label(win, text=textDiff).grid(row=0, column=0, stick='w')

textFull = "Подготовить fullmodel xml к загрузке на CIM-портал, экспортированный без применения профиля."
tk.Label(win, text=textFull).grid(row=2, column=0, stick='w')

make_diff_button('Выбрать diff').grid(row=1, column=0, padx=5, pady=5)
make_full_button('Выбрать full').grid(row=3, column=0, padx=5, pady=5)

win.mainloop()



# if __name__ == '__main__':
#     print_hi('PyCharm')
