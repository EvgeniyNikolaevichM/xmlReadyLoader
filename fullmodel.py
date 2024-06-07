from tkinter import filedialog, messagebox

lines = []


def open_file(input_file):
    global lines
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)
    return lines


def add_spaces_to_lines(line_for_add, num_spaces=6):
    space_prefix = ' ' * num_spaces
    return [space_prefix + line for line in line_for_add]


def save_file(output_file, lines_new):
    lines_for_save = add_spaces_to_lines(lines_new)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(lines_for_save)


def start_change_fullmodel():
    global output_file
    input_file = filedialog.askopenfilename(title="Выберите входной файл")
    open_file(input_file)
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
                                                   filetypes=[("Text files", "*.xml")])
    save_file(output_file, lines)
    messagebox.showinfo("Готово", "Файл обновлен и сохранен.")
