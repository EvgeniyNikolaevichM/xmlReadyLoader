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
            '  <dm:DifferenceModel>\n'
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

    def add_line_by_index(self, index, add_string):
        self.lines.insert(index, add_string + '\n')

    def update_lines(self, old_string, new_string):
        self.lines = [
            line.replace(old_string, new_string) if old_string in line else line
            for line in self.lines
        ]

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
        filtered_lines = []
        for line in self.lines:
            stripped_line = line.strip()
            remove_line = False
            for start_char, end_char in patterns:
                if stripped_line.startswith(start_char) and stripped_line.endswith(end_char):
                    remove_line = True
                    break
            if not remove_line:
                filtered_lines.append(line)
        self.lines = filtered_lines

    def remove_empty_descriptions(self):
        filtered_lines = []
        in_description_block = False
        description_block = []
        pattern_start = re.compile(r'<rdf:Description\s+[^>]*>')
        pattern_end = re.compile(r'</rdf:Description>')

        for line in self.lines:
            if not in_description_block:
                if pattern_start.search(line):
                    in_description_block = True
                    description_block = [line]
                else:
                    filtered_lines.append(line)
            else:
                description_block.append(line)
                if pattern_end.search(line):
                    in_description_block = False
                    # Check if block is empty except for the start and end tags
                    if len(description_block) == 2 and all(
                            pattern.search(l) for pattern, l in zip([pattern_start, pattern_end], description_block)):
                        continue
                    filtered_lines.extend(description_block)

        self.lines = filtered_lines

    def remove_zwnbsp(self):
        self.lines = [line.replace('\ufeff', '') for line in self.lines]
