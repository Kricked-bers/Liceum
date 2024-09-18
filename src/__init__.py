from masks import get_mask_account, get_mask_card_number
from widget import get_date, mask_account_card


print("card number or account")
answer_card_or_account = input()
if answer_card_or_account == "card":
    card_number = input("write card number: ")
    print(get_mask_card_number(card_number))
elif answer_card_or_account == "account":
    account_number = input("write account number: ")
    print(get_mask_account(account_number))
else:
    problem_number = input("write account or card: ")
    print(mask_account_card(problem_number))
