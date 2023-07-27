import json
from datetime import datetime


def get_data_from_json(name):
    """Function to retrieve data from a json file."""
    with open(name, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def sort_by_recency():
    """Function to sort data by recency."""
    data = get_data_from_json('operations.json')
    correct_data = []
    for i in data:
        if 'date' in i:
            try:
                correct_data.append(i)
            except KeyError:
                continue
    correct_data.sort(key=lambda x: x['date'], reverse=True)
    return correct_data


def five_recent_operations():
    """Function to return the 5 most recent operations."""
    data = sort_by_recency()
    five_recent_data = []
    count = 0
    while len(five_recent_data) < 5:
        if data[count]["state"] == "EXECUTED":
            five_recent_data.append(data[count])
        count += 1
    return five_recent_data


def mask_card(input_str):
    """Function to mask the card number."""
    parts = input_str.split()

    if len(parts) != 3:
        card_type, card_number = input_str.split(' ', 1)

        first_digits = card_number[:4]
        middle_digits = (f"{card_number[4:6]}** ****")
        last_digits = card_number[-4:]

        masked_card = f"{card_type} {first_digits} {middle_digits} {last_digits}"
        return masked_card

    card_type_one, card_type_two, card_number = parts

    first_digits = card_number[:4]
    middle_digits = (f"{card_number[4:6]}** ****")
    last_digits = card_number[-4:]

    masked_card = f"{card_type_one} {card_type_two} {first_digits} {middle_digits} {last_digits}"

    return masked_card


def mask_target_card(input_str):
    """Function to mask the target card number."""
    parts = input_str.split()
    if len(parts) != 3:
        card_type, card_number = input_str.split(' ', 1)

        return f"{card_type} **{card_number[-4:]}"

    card_type_one, card_type_two, card_number = parts

    return f"{card_type_one} {card_type_two} **{card_number[-4]}"


def printing():
    """Function to print operations for user."""
    for operation in five_recent_operations():
        d = datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')
        print(f"{d.strftime('%d-%m-%Y')} {operation['description']}")
        for i in operation:
            if "from" in i:
                try:
                    print(f"{mask_card(operation['from'])} -> {mask_target_card(operation['to'])}")
                except KeyError:
                    continue
        print(operation["operationAmount"]["amount"] + " " + operation["operationAmount"]["currency"]["name"] + "\n")


printing()
