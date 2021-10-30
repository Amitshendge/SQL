def function_intInput(string):
    """
Description:
    Function is used to take user input with input validation chaecks for valueError
Parameter:
      string which should be shown in terminal
Return:
       user Input
"""
    while True:
        try:
            return int(input(string))
        except ValueError:
            print('Plz enter valid integer input')
            continue

def function_strInput(string):
    """
Description:
    Function is used to take user input with input validation chaecks for valueError
Parameter:
      string which should be shown in terminal
Return:
       user Input
"""
    while True:
        try:
            return input(string)
        except ValueError:
            print('Plz enter valid integer input')
            continue
