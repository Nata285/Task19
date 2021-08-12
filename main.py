documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people_search():
    n = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == n:
            return doc['name']

    return ("нет такого номера")


def document_search():
    d = input('Введите номер документа: ')
    for num_shelf, num in directories.items():
        for num_element in num:
            if d == num_element:
                return f'документ лежит на полке номер {num_shelf}'
    return ('номер отсутствует')


def display_list():
    for doc in documents:
        return (f'{doc["type"]} "{doc["number"]}" "{doc["name"]}";')


def add_doc():
    num_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    owner_name = input('Введите имя владельца документа: ')
    num_shelf = input('Укажите номер полки для хранения документа:')
    if num_shelf in directories.keys():
        directories[num_shelf].append(num_doc)
        return (directories)
        doc = {}
        doc.setdefault('type', type_doc)
        doc.setdefault('number', num_doc)
        doc.setdefault('name', owner_name)
        documents.append(doc)
        res = documents
    else:
        res = 'Такая полка отсутствует'
    return res


def main():
    user_input = input('Выберите команду (p, s, l, a):')
    if user_input == 'p':
        return (people_search())
    elif user_input == 's':
        return (document_search())
    elif user_input == 'l':
        return (display_list())
    elif user_input == 'a':
        return (add_doc())
    else:
        return ('Такой команды нет')

if __name__ == '__main__':
    main()
