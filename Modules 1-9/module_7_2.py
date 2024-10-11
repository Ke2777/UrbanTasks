def custom_write(file_name: str, strings: list):
    with open(file_name, 'a', encoding='utf-8') as file:
        string_count = 0
        string_pos = {}
        for string in strings:
            string_count += 1
            string_pos[(string_count, file.tell())] = string
            file.write(string + '\n')
    return string_pos


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
