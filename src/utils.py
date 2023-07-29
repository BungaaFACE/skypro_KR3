import json


def get_json_data(filename: str):
    """Function returns data from json
    Args: filename (str): json filename
    Returns: list/dict: data from json
    """
    with open(filename, encoding="utf8") as json_data:
        return json.load(json_data)


def sort_operations_by_date(operations: list):
    """Function returns sorted operations by data and time
    Args: operations (list): list of operations
    Returns: (list): sorted operations
    """

    operations.sort(
        reverse=True,
        key=lambda operation: operation.get('date', '0'))
    return operations


def parse_operation_data(operation: dict):
    """
    Function parses data from operation and returns message
    Args: operation (dict): operation data
    Returns: (str): parsed message
    """

    # get datetime, cut time, reverse year and day of month
    date_list = operation.get('date', 'Дата недоступна')\
        .split('T')[0]\
        .split('-')[::-1]
    date_str = '.'.join(date_list)

    description = operation.get('description', 'Описание недоступно')

    # Define 'from' data
    if description != "Открытие вклада":
        from_data = operation.get('from', None)
        from_card_type = ' '.join(from_data.split(' ')[:-1])
        from_card_number = from_data.split(' ')[-1]
        cipher_from_card = f'{from_card_number[:4]} {from_card_number[4:6]}** **** {from_card_number[-4:]}'
    else:
        from_card_type = 'Пополнение'
        cipher_from_card = 'вклада'

    to_data = operation['to']
    to_card_type = ' '.join(to_data.split(' ')[:-1])
    cipher_to_card = f"**{to_data.split(' ')[-1][-4:]}"

    summ_str = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"

    return f"""{date_str} {description}
{from_card_type} {cipher_from_card} -> {to_card_type} {cipher_to_card}
{summ_str}
"""


def filter_operations_by_executed(operations, oper_number=3):
    """Function searches for last {oper_number} executed operations
    Args:
        operations (list): list of sorted operations
        oper_number (int, optional): number of operations to print. Defaults to 3.
    """

    filtered_operations = []
    for operation in operations:
        if operation["state"] == "EXECUTED":
            filtered_operations.append(operation)
            if len(filtered_operations) == oper_number:
                break
    return filtered_operations
