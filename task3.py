'''
3. Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления
и снятия средств в список.

Задача о банкомате из семинара 2:

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''
from typing import Dict, List


def input_command(text: str, commands: Dict[str, str]) -> str:
    while True:
        try:
            command: str = str(input(text)).upper()

            if command in commands:
                return command
            else:
                print("Такой команды не сущесвует "
                      "повторите ввод комманды")
        except ValueError:
            print("Пожалуйста повторие ввод комманды")


def show_balance(balance: float) -> None:
    print(f"На вашем счете: {balance} Рублей")


def help_program(commands: Dict[str, str]) -> None:
    for key in commands:
        print(key, " - ", commands[key])


def exit_program() -> bool:
    print("Спасибо что воспользовались нашими услугами")
    return False


def percentage_for_replenishment(count_with_repl: int,
                                 number_operations_after_plus_money: int,
                                 balance: float,
                                 growth_commission_percentage: float,
                                 history_operations: List[str]) -> float:
    if count_with_repl % number_operations_after_plus_money == 0:
        percent = (growth_commission_percentage / 100) * balance
        balance += percent
        history_operations.append(f"+{str(percent)} => начисленные проценты")

    return balance


def replenishment_balance(minimum_amount: float,
                          history_operations: List[str]) -> float:
    while True:
        try:
            command: str = input("Введите сумму пополнения счета: ")

            if command.upper() == "НАЗАД":
                return balance

            money = float(command)

            if (money % minimum_amount) == 0 and money > 0:
                history_operations.append(f"+{str(money)} => сумма пополнения")
                return money
            else:
                print("Сумма пополнения должна быть кратна 50 "
                      "и больше нуля")
                continue
        except ValueError:
            print("Вы ввели некорректное значение")


def wealth_tax(balance: float,
               wealth: float,
               wealth_commission_percentage: float,
               history_operations: List[str]) -> float:
    if balance >= wealth:
        collecting: float = ((wealth_commission_percentage / 100)
                             * balance)
        balance -= collecting
        history_operations.append(f"-{str(collecting)} => налог на богатство")

    return balance


def history_operations(history_operations: List[str]) -> None:
    for namber, history in enumerate(history_operations, start=1):
        print(str(namber) + ")", " ", history)


def adding_funds_account(minimum_amount: float,
                         balance: float,
                         minimum_amount_service: float,
                         maximum_amount_service: float,
                         servise_commission_percentage: float,
                         history_operations: List[str]) -> float:
    while True:
        try:

            command: str = input("Сколько снять со счета: ")

            if command.upper() == "НАЗАД":
                return balance

            money = float(command)

            if money % minimum_amount == 0 and money > 0:
                percent_service: float \
                    = (servise_commission_percentage / 100) * balance

                if money + percent_service <= balance:
                    if percent_service < minimum_amount_service:
                        percent_service = minimum_amount_service
                    elif percent_service > maximum_amount_service:
                        percent_service = maximum_amount_service

                    history_operations.append(f"-{str(money)} => снятая сумма\n"
                                              f"-{str(percent_service)} => "
                                              f"прощент за обслуживание")

                    return balance - money - percent_service
                else:
                    print("Вы не можете снят больше денег чем у Вас на счете \n"
                          "(учитывайте процент за обслуживание)")
            else:
                print("Сумма снятия должна быть кратна 50 "
                      "и больше нуля")
        except ValueError:
            print("Вы ввели некорректное значение")


# start


WEALTH: float = 5_000_000.00
MINIMUM_AMOUNT: float = 50.00
MINIMUM_AMOUNT_SERVISE: float = 30.00
MAXIMUM_AMOUNT_SERVISE: float = 600.00
NUMBER_OPERATION_AFTER_PLUS_MONEY: int = 3
WEALTH_COMMISSION_PERCENTAGE: float = 10.00
SERVISE_COMMISSION_PERCENTAGE: float = 1.50
GROWTH_COMMISSION_PERCENTAGE: float = 3.00

balance: float = 0.00
count_with_repl: int = 0
history_operations_list: List[str] = []

commands = {"ПОПОЛНИТЬ": "производится пополнение счета",
            "СНЯТЬ": "производится снятие средств со счета",
            "БАЛАНС": "посмотреть баланс счета",
            "ВЫЙТИ": "выход из программы",
            "ПОМОЩЬ": "доступный список комманд",
            "ИСТОРИЯ": "история операций"}

print("Для ознакомления со списком доступных комманд введите "
      "'помощь' \n (регистр при вводе комманд значения не имеет)")

flag_for_work_program: bool = True

while flag_for_work_program:

    command: str = input_command("Введите комманду: ", commands)

    balance = wealth_tax(wealth_commission_percentage=
                         WEALTH_COMMISSION_PERCENTAGE,
                         history_operations=
                         history_operations_list,
                         balance=balance,
                         wealth=WEALTH)

    match command:
        case "ПОПОЛНИТЬ":
            show_balance(balance)
            balance += replenishment_balance(minimum_amount=
                                             MINIMUM_AMOUNT,
                                             history_operations=
                                             history_operations_list)
            count_with_repl += 1
            balance = percentage_for_replenishment(number_operations_after_plus_money=
                                                   NUMBER_OPERATION_AFTER_PLUS_MONEY,
                                                   growth_commission_percentage=
                                                   GROWTH_COMMISSION_PERCENTAGE,
                                                   history_operations=
                                                   history_operations_list,
                                                   count_with_repl=
                                                   count_with_repl,
                                                   balance=balance)
        case "СНЯТЬ":
            show_balance(balance)
            balance = adding_funds_account(servise_commission_percentage=
                                           SERVISE_COMMISSION_PERCENTAGE,
                                           minimum_amount_service=
                                           MINIMUM_AMOUNT_SERVISE,
                                           maximum_amount_service=
                                           MAXIMUM_AMOUNT_SERVISE,
                                           history_operations=
                                           history_operations_list,
                                           minimum_amount=
                                           MINIMUM_AMOUNT,
                                           balance=balance)
            count_with_repl += 1
            balance = percentage_for_replenishment(number_operations_after_plus_money=
                                                   NUMBER_OPERATION_AFTER_PLUS_MONEY,
                                                   growth_commission_percentage=
                                                   GROWTH_COMMISSION_PERCENTAGE,
                                                   history_operations=
                                                   history_operations_list,
                                                   count_with_repl=
                                                   count_with_repl,
                                                   balance=balance)
        case "БАЛАНС":
            show_balance(balance)
        case "ПОМОЩЬ":
            help_program(commands)
        case "ВЫЙТИ":
            flag_for_work_program = exit_program()
        case "ИСТОРИЯ":
            history_operations(history_operations=
                               history_operations_list)

# stop
