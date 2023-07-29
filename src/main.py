from src.utils import get_json_data, sort_operations_by_data, print_last_operations

OPERATIONS_FILE = "./src/operations.json"
GET_OPERATIONS_NUMBER = 5


def main(operations_file, num_of_oper):
    """
    Function starts programm
    Args:
        operations_file (str): name of json with operations
        num_of_oper (int): number of operations to display
    """

    # Get operations from json
    operations_list = get_json_data(operations_file)
    # Sort operations by date and time
    sorted_operations = sort_operations_by_data(operations_list)
    # Print last {num_of_oper} of operations
    print_last_operations(sorted_operations, num_of_oper)


if __name__ == "__main__":
    main(OPERATIONS_FILE, GET_OPERATIONS_NUMBER)
