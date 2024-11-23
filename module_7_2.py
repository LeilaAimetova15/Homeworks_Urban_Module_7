def custom_write(file_name: str, strings: list):
    strings_positions = {}
    number_of_line = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        byte_of_line = file.tell()
        file.write(f'{i}\n')
        strings_positions[(number_of_line, byte_of_line)] = i
        number_of_line += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)