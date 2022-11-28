from os import system

def display_help():
    print("Commands (not sensitive to case):",
            "'Exit' - Exits the game",
            "'Set:row,column,value' - changes number in given row and colum to a given value, indexing from 0",
            "'Help' - displays this message",
            sep="\n")

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

    terminate=False
    help_needed=False
    while not terminate:
        system('cls')
        display_sudoku(active_sudoku)
        if help_needed:
            display_help()
            help_needed=False
        control=input()
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
            help_needed=True
    print("finished")


main_loop()

