"""
Using A dictionary to perform a python equivalent of a switch statement

"""


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

print(math_operation("mul", 2, 3))

