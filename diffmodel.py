from tkinter import filedialog, messagebox

from base import BaseClass

patterns = [
    ('<me:', '>'),
    ('<rh:', '>'),
    ('<cim17:', '>')
]


def ready_diff_model():
    input_file = filedialog.askopenfilename(title="Выберите входной файл")
    old_string = '<dm:reverseDifferences>\n'
    new_string = '<dm:reverseDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">\n'
    old_string2 = '<dm:forwardDifferences>\n'
    new_string2 = '<dm:forwardDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">\n'
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
                                                   filetypes=[("Text files", "*.xml")])
        if output_file:
            obj = BaseClass()
            obj.open_file(input_file)
            obj.remove_lines_start(9)
            obj.add_header_lines()
            obj.remove_me_class_name()
            obj.remove_by_patterns(patterns)
            obj.update_lines(old_string, new_string)
            obj.update_lines(old_string2, new_string2)
            obj.save_file(output_file)
            messagebox.showinfo("Готово", "Файл обновлен и сохранен.")
        else:
            messagebox.showwarning("Ошибка", "Файл для сохранения не выбран.")
    else:
        messagebox.showwarning("Ошибка", "Входной файл не выбран.")
