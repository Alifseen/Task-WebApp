""" Added in section 15"""
FILEPATH = "todos.txt"
""" Defining this constant makes it easier to change the file path if needed in the future"""


def get_todo_list(filepath=FILEPATH):
    """ Read the text file and return the content in a variable as a list"""
    with open(filepath) as file:
        todoTxtFile = file.readlines()
        return todoTxtFile


def set_todo_list(set_list, filepath=FILEPATH):
    """ Writes content as a list to a text file"""
    with open(filepath, "w") as file:
        file.writelines(set_list)

""" Added in section 14 """
if __name__ == "__main__":
    """__name__ is a hidden variable defined by python that stores __main__ is the program is calling itself, otherwise it changes to the name of the python file."""
    print(get_todo_list())