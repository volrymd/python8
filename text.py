# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def show_menu():
    print('1. Распечатать справочник\n'
        '2. Найти телефон по фамилии\n'
        '3. Изменить номер телефона\n'
        '4. Удалить запись\n'
        '5. Найти абонента по номеру телефона\n'
        '6. Добавить абонента в справочник\n'
        '7. Закончить работу')
    choice=int(input())
    return choice

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    with open('phonebook.txt','r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename,phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    for line in phone_book:
        print (line, end= "\n")
    return phone_book

def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        for v in i.values():
            if v == last_name:
               return i

def change_number(phone_book,last_name,new_number):
    for i in phone_book:
        for v in i.values():
            if v == last_name:
               i["Телефон"] = new_number
               return phone_book

def delete_by_lastname(phone_book, lastname):
    for i in phone_book:
        for v in i.values():
            if v == lastname:
               phone_book.remove(i)
               return phone_book

def find_by_number(phone_book,number):
    for i in phone_book:
        for v in i.values():
            if v == number:
               return i

def add_user(phone_book, user_data):
    input1 = user_data.split()
    input2 = input('Введите описание: ')
    input1.append(input2)
    list1 = ['Фамилия', 'Имя', 'Отчество', 'Номер', 'Описание']
    result1 = dict(zip(list1, input1))
    phone_book.append(result1)
    return phone_book

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
            write_txt('phonebook.txt',phone_book)
        elif choice==4:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
            write_txt('phonebook.txt',phone_book)
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('Введите через пробел: Фамилия, Имя, Отчество, Номер: ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        
        choice=show_menu()
    
work_with_phonebook()



