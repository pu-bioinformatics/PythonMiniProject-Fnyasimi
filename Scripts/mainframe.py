#! /bin/python

"""The module contains a function that controls the function of the pdb explorer ensuring a pdb file should be present for different options to work"""

def mainframe(opt,pdb):
    """
    The function controls what happens when a user selects an option
    Arguments: opt (short form for selected option).
    If the option does not exist it returns to the menu screen"""
    
    global path
    
    #Import required modules
    from menu import menuscreen
    from filecheck import filecheck
    from information import pdb_info
    from histogram import aminoacid_histogram
    from sec_structure import secondary_structure
    from export import pdb_export
    from exitloop import exitloop
    
    if opt == 'O': # Open file
        if pdb == "None": # No loaded pdb file
            pdb, path = filecheck(pdb) # Load file
            menuscreen(pdb)

        else: # If there is a loaded file you want to replace 
            print("     File %s is loaded, do you want to replace the file?" %pdb)
            replace = input("     Y/N: ")
            replace = replace.upper()
            
            if replace == 'Y':
                pdb, path = filecheck(pdb)
                menuscreen(pdb)
            
            if replace == 'N':
                menuscreen(pdb)
            
            if replace != 'Y' and replace != 'N':
                replace = input("     Invalid option please input Y/N: ")
                replace = replace.upper()
                
                while replace != 'Y' and replace != 'N':
                    replace = input("     Invalid option please input Y/N: ")
                    replace = replace.upper()

                    if replace == 'Y':
                        pdb, path = filecheck(pdb)
                        menuscreen(pdb)
                        
                    if replace == 'N':
                        menuscreen(pdb)
                    
    else:
        if opt == 'I' or opt == 'H' or opt == 'S' or opt == 'X' or opt == 'Q':
            if pdb == "None":
                if opt == 'Q':
                    exitloop(pdb)
                else:
                    print("     There is no file loaded, do you want to load a file?")
                    new = input("     Y/N: ")
                    new = new.upper()
                    
                    if new == 'Y':
                        pdb, path = filecheck(pdb)
                        menuscreen(pdb)
                    if new == 'N':
                        menuscreen(pdb)
                        
                    if new != 'Y' and new != 'N':
                        new = input("     Invalid option please input Y/N: ")
                        new = new.upper()
                
                        while new != 'Y' and new != 'N':
                            new = input("     Invalid option please input Y/N: ")
                            new = new.upper()

                            if new == 'Y':
                                pdb, path = filecheck(pdb)
                                menuscreen(pdb)

                            if new == 'N':
                                menuscreen(pdb)
                        
            else:
                if opt == 'I':
                    pdb_info(path,pdb) # Information function
                    menuscreen(pdb)
                if opt == 'H':
                    aminoacid_histogram(path) # amino histogram function
                    menuscreen(pdb)
                if opt == 'S':
                    secondary_structure(path, pdb) # Show secondary structure of a protein
                    menuscreen(pdb)
                if opt == 'X':
                    pdb_export(path)
                    menuscreen(pdb)
                if opt == 'Q':
                    exitloop(pdb) #exit function
        else:
            print("     Invalid option entered")
            menuscreen(pdb)
