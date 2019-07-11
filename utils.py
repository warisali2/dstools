def to_arr_format(string):
    """
    Converts newline separated string of items to coma separated string of items
    :param string: newline separated string of items
    :return: comma separated string of items
    """
    return "'" + string.replace('\n', "', '")[:-3]
