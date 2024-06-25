from tkinter import filedialog, simpledialog, messagebox
from base import BaseClass

default_patterns = [
    ('<me:', '>'),
    ('<rh:', '>'),
    ('<cim17:', '>')
]


def ready_custom_model():
    input_file = filedialog.askopenfilename(title="Выберите входной файл")
    if input_file:
        output_file = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".xml",
                                                   filetypes=[("Text files", "*.xml")])
        if output_file:
            use_defaults = messagebox.askyesno("Использовать значения по умолчанию?",
                                               "Удалить теги me: rh: cim17:?")
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

            delete_me_class_name = messagebox.askyesno("Удаление me:class у description",
                                                       "Удалить me:class у description?")
            flag = True
            if delete_me_class_name:
                flag = True
            else:
                flag = False

            add_lines = messagebox.askyesno("Добавление строк",
                                            "Добавить строку по индексу?")
            if add_lines:
                index = simpledialog.askinteger("Ввод", "Введите индекс для добавления строки:")
                add_string = simpledialog.askstring("Ввод", "Введите строку для добавления:")
            else:
                index = None
                add_string = None

            replace_lines = messagebox.askyesno("Замена строк",
                                                "Заменить строку по точному совпадению?")
            if replace_lines:
                old_string = simpledialog.askstring("Ввод", "Введите строку для замены:")
                new_string = simpledialog.askstring("Ввод", "Введите новую строку для замены:")
            else:
                old_string = None
                new_string = None

            if patterns:
                obj = BaseClass()
                obj.open_file(input_file)
                obj.remove_zwnbsp()
                obj.remove_by_patterns(patterns)
                if flag is not False:
                    obj.remove_me_class_name()
                if index is not None and add_string is not None:
                    obj.add_line_by_index(index, add_string)
                if old_string is not None and new_string is not None:
                    obj.update_lines(old_string, new_string)
                obj.save_file(output_file)
                messagebox.showinfo("Готово", "Файл обновлен и сохранен.")
            else:
                messagebox.showwarning("Предупреждение", "Не были заданы пары символов для удаления строк.")
    else:
        messagebox.showwarning("Ошибка", "Входной файл не выбран.")
