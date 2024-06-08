import re


class BaseClass:
    def __init__(self):
        self.lines = []

    def open_file(self, input_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            self.lines = file.readlines()

    def save_file(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(self.lines)

    def add_spaces_to_lines(self, num_spaces=4):
        space_prefix = ' ' * num_spaces
        self.lines = [space_prefix + line for line in self.lines]

    def add_header_lines(self):
        lines_to_add = [
            '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n',
            '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
            'xmlns:so="http://so-ups.ru/2015/schema-cim16#" xmlns:cim="http://iec.ch/TC57/CIM100#" '
            'xmlns:dm="http://iec.ch/TC57/61970-552/DifferenceModel/1#" xmlns:rf="http://gost.ru/2019/schema-cim01#" '
            'xmlns:ups="https://cim.so-ups.ru#" xml:base="">\n',
            '  <dm:DifferenceModel>\n',
            '    <dm:forwardDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">\n'
        ]
        self.lines = lines_to_add + self.lines

    def add_footer_lines_for_full(self):
        lines_to_add = [
            '    </dm:forwardDifferences>\n',
            '    <dm:reverseDifferences rdf:parseType="Statements" xml:base="https://cim.so-ups.ru#">\n',
            '    </dm:reverseDifferences>\n',
            '  </dm:DifferenceModel>\n',
            '</rdf:RDF>\n',
        ]
        self.lines = self.lines + lines_to_add

    def remove_lines_start(self, count_start):
        self.lines = self.lines[count_start:]

    def remove_lines_end(self, count_end):
        self.lines = self.lines[:count_end]

    def remove_me_class_name(self):
        updated_lines = []
        for line in self.lines:
            line = re.sub(r'(me:className="[^"]*")', '', line)
            updated_lines.append(line)
        self.lines = updated_lines

    def remove_by_patterns(self, patterns):
        patterns = [
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
        for line in self.lines:
            line = line.strip()
            remove_line = False
            for start_char, end_char in patterns:
                if line.startswith(start_char) and line.endswith(end_char):
                    remove_line = True
                    break
            if not remove_line:
                self.lines.append(line)

    def update_lines(self, old_string, new_string):
        self.lines = [
            new_string if line == old_string else
            line
            for line in self.lines
        ]

    # def add_and_save_lines(output_file, add_string, index, add_string2, index2, add_string3, index3):
    #     global updated_lines
    #     updated_lines.insert(index, add_string + '\n')
    #     updated_lines.insert(index2, add_string2 + '\n')
    #     updated_lines.insert(index3, add_string3 + '\n')
    #     with open(output_file, 'w', encoding='utf-8') as file:
    #         file.writelines(updated_lines)
    #
    #
    # def select_file(default_patterns, old_string1, new_string1, old_string2, new_string2, add_string, index, add_string2,
    #                 index2, add_string3, index3):
    #     input_file = filedialog.askopenfilename(title="Выберите входной файл")
    #     if input_file:
    #         output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
    #                                                    filetypes=[("Text files", "*.xml")])
    #         if output_file:
    #             use_defaults = messagebox.askyesno("Использовать значения по умолчанию?",
    #                                                "Хотите использовать кортежи символов для удаления по умолчанию?")
    #             if use_defaults:
    #                 patterns = default_patterns
    #             else:
    #                 patterns = []
    #                 while True:
    #                     start_char = simpledialog.askstring("Ввод",
    #                                                         "Введите начальный символ (или оставьте пустым для завершения):")
    #                     if not start_char:
    #                         break
    #                     end_char = simpledialog.askstring("Ввод",
    #                                                       "Введите конечный символ (или оставьте пустым для завершения):")
    #                     if not end_char:
    #                         break
    #                     patterns.append((start_char, end_char))
    #             if patterns:
    #                 remove_lines(input_file, patterns)
    #                 remove_me_class_name()
    #                 update_lines(old_string1, new_string1, old_string2, new_string2)
    #                 add_and_save_lines(output_file, add_string, index, add_string2, index2, add_string3, index3)
    #                 messagebox.showinfo("Готово", "Строки успешно удалены/обновлены и файл сохранен.")
    #             else:
    #                 messagebox.showwarning("Предупреждение", "Не были заданы пары символов для удаления строк.")

