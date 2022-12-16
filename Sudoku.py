from os import system

def help_message() -> str:
    message = "Commands (not sensitive to case): \n"+ \
            "'Exit' - Exits the game \n"+ \
            "'Set:row,column,value' - changes number in given row and colum to a given value, indexing from 0 \n"+ \
            "'Help' - displays this message \n"+\
            "'Check' - checks if sudoku is properly filled \n"+\
            "'Raw' - displays sudoku in raw numeric form \n"+\
            "'Load: path' - loads sudoku form text file at given path \n"+\
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

def display_raw_sudoku(sudoku:list[list[int]]):
    
    for row in sudoku:
        for element in row:
                print(element,end="")
        print()

def load_sudoku(file:str) ->list[list[int]]:
    loaded_sudoku=[]
    row=0
    column=0
    with open(file) as f:
        for line in f:

            line=line.strip().strip("\n")
            #print("|",line,"|",sep="")
            loaded_sudoku.append([])
            for element in line:
                #print(row,column, element)
                loaded_sudoku[row].append(int(element))
                column+=1
            
            row+=1
            column=0
    return loaded_sudoku

        

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


def main_loop():

    active_sudoku = load_sudoku("example_sudoku.txt")
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
        elif control == "raw" or control == "Raw":
            display_raw_sudoku(active_sudoku)
            input("press Enter key to continue")
        elif control.startswith("load:") or control.startswith("Load:"):
            active_sudoku=load_sudoku(control.lower().strip("load:").strip())
            #input("press Enter key to continue")

    print("finished")


main_loop()

