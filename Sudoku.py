from os import system

def help_message() -> str:
    message = "Commands (not sensitive to case): \n"+ \
            "'Exit' - Exits the game \n"+ \
            "'Set:row,column,value' - changes number in given row and colum to a given value, indexing from 0 \n"+ \
            "'Help' - displays this message \n"+\
            "'Check' - checks if sudoku is properly filled \n"+\
            "\n"
    return message

def display_sudoku(sudoku:list[list[int]]):
    print("-"*18)
    for row in sudoku:
        print("|", end="")
        for element in row:
            if element==0:
                print(" ",end="")
            else:
                print(element,end="")
            print("|",end="")
        print()
        print("-"*18)

def attendance(attendance_list:list[int]) -> int:
    total = 1
    for number in attendance_list:
        total *= number
    return total

def check_sudoku(sudoku:list[list[int]]) -> bool:
    attendance_list = [0,0,0,0,0,0,0,0,0] #list for checking presence of numbers

    #check rows
    for row in sudoku:
        attendance_list = [1,0,0,0,0,0,0,0,0,0]
        for element in row:
            attendance_list[element] += 1
        if attendance(attendance_list)!=1:
            return False
    
    #check columns
    for i in range(9):
        attendance_list = [1,0,0,0,0,0,0,0,0,0]
        for j in range(9):
            element=sudoku[j][i]
            attendance_list[element] += 1
        if attendance(attendance_list)!=1:
            return False

    #check boxes
    for i in range(9):
        attendance_list = [1,0,0,0,0,0,0,0,0,0]
        for j in range(9):
            row = 3*(i // 3) + (j // 3)
            column = 3*(i % 3) + (j % 3)
            element=sudoku[row][column]
            attendance_list[element] += 1
        if attendance(attendance_list)!=1:
            return False
    return True


example_sudoku=[[0,0,8,0,0,0,0,4,0],
                [0,6,0,0,0,3,0,0,0],
                [2,0,0,0,5,0,1,0,8],
                [0,0,0,0,0,0,0,0,9],
                [8,0,0,0,1,0,7,0,5],
                [0,0,2,8,0,0,0,0,0],
                [0,0,0,0,4,0,0,2,0],
                [0,0,3,0,0,5,4,0,7],
                [7,0,0,0,0,0,0,9,0],]


def main_loop():

    active_sudoku = example_sudoku
    message=help_message()
    terminate=False

    while not terminate:
        system('cls')
        display_sudoku(active_sudoku)
        
        print(message,end="")
        message=""

        control=input("Awaiting command: ")
        if control=="exit" or control == "Exit":
            terminate=True
        elif control.startswith("set:") or control.startswith("Set:"):
            command=control
            command = command.lower().strip("set:").strip()
            row = int(command[0])
            column = int(command[2])
            value = int(command[4])
            active_sudoku[row][column]=value
        elif control=="help" or control=="Help":
            message=help_message()
        elif control == "Check" or control == "check":
            if check_sudoku(active_sudoku):
                message = "Sudoku all right \n"
            else:
                message = "Sudoku wrong \n"
    print("finished")


main_loop()

