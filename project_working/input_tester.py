import os
from getch import getch

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    in_list = ["1", "2"]
    clear_screen()
    print()
    while True:



        clear_screen()
        print("1: Start\n2: Instructions" )
        in_put = getch()
        print(in_put)

        if in_put == "2":

            clear_screen()
            print()
            print("You have chosen option 2")
            print("Press space for the main menu")
            in_put = getch()
            if in_put =="":
                break

        elif in_put =="1":


            clear_screen()
            print()
            print("You have chosen option 1")

            break
        elif in_put not in in_list:
            continue
        else:
            break


    #main_loop()
if __name__ == "__main__":
    main()
