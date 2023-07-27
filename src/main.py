from funcs import *

transaction = "operations.json"


def main(transactions):
    """
    Main function
    """
    printing(five_recent_operations(sort_by_recency(get_data_from_json(transactions))))


if __name__ == "__main__":
    main(transaction)
