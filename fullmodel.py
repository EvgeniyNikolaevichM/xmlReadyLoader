from tkinter import filedialog, messagebox

from base import BaseClass

patterns = [
    ('<md:Model.created>', '>'),
    ('<md:Model.description>', '>'),
    ('<md:Model.version>', '>'),
    ('<me:Model.name>', '>'),
    ('<md:FullModel', '>'),
    ('</md:FullModel>', '>'),
    ('<me:', '>'),
    ('<rh:', '>'),
    ('<cim17:', '>'),
    ('</me:', '>'),
    ('</rh:', '>'),
    ('</cim17:', '>'),
    ('<cim:IdentifiedObject.name>Роли', '>'),
]


def convert_to_diff():
    input_file = filedialog.askopenfilename(title="Выберите входной файл")
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
                                                   filetypes=[("Text files", "*.xml")])
        if output_file:
            obj = BaseClass()
            obj.open_file(input_file)
            obj.add_spaces_to_lines()
            obj.remove_lines_start(4)
            obj.remove_lines_end(-1)
            obj.remove_by_patterns(patterns)
            obj.add_header_lines()
            obj.add_footer_lines_for_full()
            obj.add_line_by_index(3,
                                  '    <dm:forwardDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">')
            obj.save_file(output_file)
            messagebox.showinfo("Готово", "Файл обновлен и сохранен.")
        else:
            messagebox.showwarning("Ошибка", "Файл для сохранения не выбран.")
    else:
        messagebox.showwarning("Ошибка", "Входной файл не выбран.")
