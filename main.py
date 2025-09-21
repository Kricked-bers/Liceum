from src.processing import filter_by_state, sort_by_date
from src.utils import searching_for_json_file
from src.file_analyzer import csv_analyzer, xls_analyzer
from src.generators import filter_by_currency
from src.file_analyzer import re_search_string
from src.widget import get_date, mask_account_card

directory_json = r'C:\Users\islam\PycharmProjects\Liceum\data\operations.json'
directory_csv = r'C:\Users\islam\PycharmProjects\Liceum\data\transactions.csv'
directory_xls = r'C:\Users\islam\PycharmProjects\Liceum\data\transactions_excel.xlsx'
print("Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.")
print("Выберите необходимый пункт меню:")
print("1. Получить информацию о транзакциях из JSON-файла")
print("2. Получить информацию о транзакциях из CSV-файла")
print("3. Получить информацию о транзакциях из XLSX-файла")
file_type = str()
while True:
    try:
        transactions = list()
        client_inf_file = int(input("Пользователь: "))
        if client_inf_file == 1:
            print("Программа: Для обработки выбран JSON-файл.")
            transactions = searching_for_json_file(directory_json)
            file_type = "JSON"
        elif client_inf_file == 2:
            print("Программа: Для обработки выбран CSV-файл.")
            transactions = csv_analyzer(directory_csv)
            file_type = "CSV"
        elif client_inf_file == 3:
            print("Программа: Для обработки выбран XLSX-файл.")
            transactions = xls_analyzer(directory_xls)
            file_type = "XLSX"
        else:
            print("Введен неккоректный ответ. Попробуйте еще раз.")
            continue
        break
    except Exception:
        print("Введен неккоректный ответ. Попробуйте еще раз.")

print("Программа: Введите статус, по которому необходимо выполнить фильтрацию. \n"
      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
while True:
    client_inf_state = input("Пользователь: ")
    if client_inf_state.lower() == "executed":
        print('Программа: Операции отфильтрованы по статусу "EXECUTED"')
    elif client_inf_state.lower() == "canceled":
        print('Программа: Операции отфильтрованы по статусу "CANCELED"')
    elif client_inf_state.lower() == "pending":
        print('Программа: Операции отфильтрованы по статусу "PENDING"')
    else:
        print(f'Программа: Статус операции "{client_inf_state}" недоступен.')
        continue
    break
filtered_transactions = filter_by_state(transactions, client_inf_state.upper())

while True:
    question_transactions = filtered_transactions
    print("Программа: Отсортировать операции по дате? Да/Нет")
    ques_sort_by_date = input("Пользователь: ")
    if ques_sort_by_date.lower() == "да":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        ques_sort_up_down = input("Пользователь: ")
        if ques_sort_up_down.lower() == "по возрастанию":
            question_transactions = sort_by_date(question_transactions, "True")
        elif ques_sort_up_down.lower() == "по убыванию":
            question_transactions = sort_by_date(question_transactions, "False")
        else:
            print("Некорректный ответ. Попробуйте снова")
            continue
    elif ques_sort_by_date.lower() != "нет":
        print("Некорректный ответ. Попробуйте снова")
        continue

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    ques_rub_trans = input("Пользователь: ")
    if ques_rub_trans.lower() == "да":
        if file_type == "JSON":
            question_transactions = list(filter_by_currency(question_transactions, 'RUB'))
        elif file_type == "CSV" or file_type == "XLSX":
            question_transactions = list(filter_by_currency(question_transactions, 'RUB', file_type))
    elif ques_rub_trans.lower() != "нет":
        print("Некорректный ответ. Попробуйте снова")
        continue

    print("Программа: Отфильтровать список транзакций по определенному слову "
          "в описании? Да/Нет")
    ques_filter_by_desk = input("Пользователь: ")
    if ques_filter_by_desk.lower() == "да":
        while True:
            print("Программа: Введите слово для фильтрации")
            ques_filter_by_desk_word = input("Пользователь: ")
            question_transactions = re_search_string(question_transactions, ques_filter_by_desk_word)
            if len(question_transactions) == 0:
                print("Программа: Отсутствуют транзакции с заданным словом в описании."
                      "Попробуйте еще раз")
                continue
            else:
                break
    elif ques_filter_by_desk.lower() != "нет":
        print("Некорректный ответ. Попробуйте снова")
        continue
    print("Программа: Распечатываю итоговый список транзакций...")
    if len(question_transactions) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши "
              "условия фильтрации")
        break
    if file_type == "JSON":
        for transaction in question_transactions:
            print(f'{get_date(transaction["date"], "d.m.Y")} {transaction["description"]}')
            if "from" in transaction.keys():
                print(f'{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}')
            else:
                print(mask_account_card(transaction['to']))
            print(f'Сумма: {transaction["operationAmount"]["amount"]} '
                  f'{transaction["operationAmount"]["currency"]['code']}')
        break
    else:
        for transaction in question_transactions:
            print(f'{get_date(transaction["date"], "d.m.Y")} {transaction["description"]}')
            if "from" in transaction.keys() and transaction['from']:
                print(f'{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}')
            else:
                print(mask_account_card(transaction['to']))
            print(f'Сумма: {transaction["amount"]} '
                  f'{transaction["currency_code"]}')
        break