#! /bin/python

def filecheck ():
    
    global pdb,path,filename
    
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
            myfile.close()
            if line_1.startswith("HEADER"):
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
    
    
    return pdb, path, filename