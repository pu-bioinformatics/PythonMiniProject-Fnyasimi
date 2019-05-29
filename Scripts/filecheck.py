#! /bin/python

"""The module contains the function which checks if the file exists and loads it for analysis"""

def filecheck(pdb):
    
    """The main file loader function for the pdb explorer.
    Prompts the user to input the path to the pdb file. It checks if the path is correct and if the file exists.
    If all are correct its accepted
    Arguments: pdb for udating the current file otherwise unchanged."""
    
    import os # os is used to check if path and files are true
    
    path = input ("Enter a Valid PATH for a PDB File: ")
    
    # Split the path to obtain the file directory and file name
    path1 = path.split("/")
    directory = "/".join(path1[:-1])
    filename = path1[-1]
    
    # Checking if path and file are true
    if os.path.isdir(directory):
        if os.path.isfile(path):
            myfile = open(path,"r")
            line_1 = myfile.readline()
            lastline = myfile.readlines()[-1]
            myfile.close()
            #all pdb files start with header and have a length of 81 and lastline starts with end
            if line_1.startswith("HEADER") and len(line_1) == 81 and lastline.startswith("END"): 
                print("The File %s has been successfully loaded" %filename)
                pdb = filename # reassign the name of the pdb file to update on menu screen
            
            else:
                print("This is not a pdb file")
                
        else:
            extension = filename.split(".")
            if extension[-1] == 'pdb':
                print("The File %s does not exist" %filename)
                
            else:
                print("The File %s is not a pdb file" %filename)
                
    else:
        print("The directory does not exist ")
     
    return pdb, path