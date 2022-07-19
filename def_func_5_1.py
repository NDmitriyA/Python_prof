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


def get_name():
    number = input('Введите номер документа: ')
    for data in documents:
        if data.get("number") == number:
            return print(data.get('name'))
    return print('Документа с таким номером нет')


def get_shelf_number():
    number = input('Введите номер документа: ')
    for key in directories:
        if number in directories.get(key):
            return print(key)
    return print('В полках документа с данным номером нет.')


def get_list_doc(documents):
    for doc in documents:
        print(f"{doc['type']} {doc['number']} {doc['name']};")


def add_doc():
    shelf = input('Введите номер полки куда положить документ: ')
    if shelf not in directories:
        return print('Нет такой полки')
    doc = {}
    for info in ('type', 'number', 'name'):
        doc[info] = input(f'{info}: ')
        directories[shelf] = [doc['number']]
        documents.append(doc)
        return print('Документ добавлен')


while True:
    print('Возможные команды: p, s, l, a')
    comand = input('Введите название команды ')

    if comand == 'p':
        get_name()

    elif comand == 's':
        get_shelf_number()

    elif comand == 'l':
        get_list_doc(documents)

    elif comand == 'a':
        add_doc()
