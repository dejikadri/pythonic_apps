"""
Using A dictionary to perform a python equivalent of a switch statement

"""
operation_to_perform = input('enter the operator (add(ition), sub(traction), mul(tiplication), div(vision)): ')

try:
    first_int = int(input('Enter First Integer: '))
    second_int = int(input('Enter Second Integer: '))
except Exception as err:
    print(f'Somethings Wrong... : {err}')
    exit()

def math_operation(operator, first_integer, second_integer):
    """

    :param operator: either addition, subtraction, multiplication and division
    :param a: integer
    :param b: integer
    :return: result of operator on the integers
    """
    s_dict = {
        "add": lambda: first_integer + second_integer,
        "sub": lambda: first_integer - second_integer,
        "mul": lambda: first_integer * second_integer,
        "div": lambda: first_integer / second_integer,

    }
    result = s_dict.get(operator, lambda: "No Such Operator")()
    return result

try:
    print(f' Result is: {math_operation(operation_to_perform, first_int, second_int)}')
except Exception as err:
    print(f'Somethings Wrong... : {err}')

