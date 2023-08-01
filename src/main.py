import add_parent_dir_to_path
from src.utils import get_json_data, sort_operations_by_date, filter_operations_by_executed, parse_operation_data

OPERATIONS_FILE = './src/operations.json'
GET_OPERATIONS_NUMBER = 5


def main(operations_file, num_of_oper):
    """
    Function starts programm
    Args:
        operations_file (str): name of json with operations
        num_of_oper (int): number of operations to display
    """

    operations_list = get_json_data(operations_file)
    sorted_operations = sort_operations_by_date(operations_list)

    # Filter operations by EXECUTED state
    filtered_operations = filter_operations_by_executed(
        sorted_operations, num_of_oper)

    for operation in filtered_operations:
        print(parse_operation_data(operation))


if __name__ == "__main__":
    main(OPERATIONS_FILE, GET_OPERATIONS_NUMBER)
