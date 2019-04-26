#! /bin/python

def mainframe(opt):
    """
    The function controls what happens when a user selects an option
    Arguments: opt (short form for selected option).
    If the option does not exist it returns to the menu screen"""
    
    if opt == 'O': # Open file
        if pdb == "None": # No loaded pdb file
            filecheck() # Load file
            menuscreen()

        else: # If there is a loaded file you want to replace 
            print("File %s is loaded, do you want to replace the file?" %pdb)
            replace = input("Y/N: ")
            replace = replace.upper()
            
            if replace == 'Y':
                filecheck()
                menuscreen()
            
            if replace == 'N':
                menuscreen()
            
            if replace != 'Y' and replace != 'N':
                replace = input("Invalid option please input Y/N: ")
                replace = replace.upper()
                
                while replace != 'Y' and replace != 'N':
                    replace = input("Invalid option please input Y/N: ")
                    replace = replace.upper()

                    if replace == 'Y':
                        filecheck()
                        menuscreen()
                        
                    if replace == 'N':
                        menuscreen()
    else:
        if opt == 'I' or opt == 'H' or opt == 'S' or opt == 'X' or opt == 'Q':
            if pdb == "None":
                if opt == 'Q':
                    exitloop()
                else:
                    print("There is no file loaded, do you want to load a file?")
                    new = input("Y/N: ")
                    new = new.upper()
                    
                    if new == 'Y':
                        filecheck()
                        menuscreen()
                    if new == 'N':
                        menuscreen()
                        
                    if new != 'Y' and new != 'N':
                        new = input("Invalid option please input Y/N: ")
                        new = new.upper()
                
                        while new != 'Y' and new != 'N':
                            new = input("Invalid option please input Y/N: ")
                            new = new.upper()

                            if new == 'Y':
                                filecheck()
                                menuscreen()

                            if new == 'N':
                                menuscreen()
            else:
                if opt == 'I':
                    pdb_info(path) # Information function
                    menuscreen()
                if opt == 'H':
                    aminoacid_histogram() # amino histogram function
                    menuscreen()
                if opt == 'S':
                    secondary_structure(path) # Show secondary structure of a protein
                    menuscreen()
                if opt == 'X':
                    pdb_export(path)
                    menuscreen()
                if opt == 'Q':
                    exitloop() #exit function
        else:
            print("Invalid option entered")
            menuscreen()