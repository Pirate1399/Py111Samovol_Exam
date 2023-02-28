def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    open_bracket = 0

    for i in brackets_row:
        if i == "(":
            open_bracket += 1
        elif i == ")":
            open_bracket -= 1
        if open_bracket < 0:
            return False

    if open_bracket == 0:
        return True
    return False
