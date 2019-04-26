#! /bin/python

def exitloop():
    """
    The function is used when the user wants to exit the program.
    It ensures the user only inputs the right option (M or E), otherwise all other options will not work.
    Option M returns the user to menu screen.
    Option E quits the program."""
    
    exit = input("Do you want to exit(E) or do you want go back to the menu (M): ")
    exit = exit.upper()
    
    if exit == 'M':
        menuscreen()
    if exit == 'E':
        print("Thank you the pdb file explorer has exited.") 
    if exit != 'M' and exit != 'E':
        exit = input("Do you want to exit(E) or do you want go back to the menu (M): ")
        exit = exit.upper()
        while exit != 'M' and exit != 'E':

            exit = input("Do you want to exit(E) or do you want go back to the menu (M): ")
            exit = exit.upper()
            if exit == 'M':
                menuscreen()
            if exit == 'E':
                print("Thank you the pdb file explorer has exited.")       
      
