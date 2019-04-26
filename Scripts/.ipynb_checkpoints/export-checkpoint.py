#! /bin/python

def pdb_export(path):
    """This function exports the current loaded pdb file into a new file in the defined path.
    Arguments: User inputs path and the new pdb filename"""
    
    import os
    out_path = input ("""
    Enter a Valid PATH to where you want to export the file and the new filename.pdb 
    :""")

    # Split the path to obtain the file directory and new filename
    out_path1 = out_path.split("/")
    directory = "/".join(out_path1[:-1])
    filename = out_path1[-1]

    # Checking if path exists
    if os.path.isdir(directory):

        name_tag = False
        extension = filename.split(".")

        if len(extension) == 1: # checking if the extention is included
            filename = filename + ".pdb"
            out_path = directory + "/" + filename
            name_tag = True

        else:
            if len(extension) == 2 and extension[-1] == 'pdb': # confirm right naming
                name_tag = True
            else:
                print("Check your output filename and rename it appropriately")
                pdb_export(path)

        if name_tag:
            #open file for writing and export
            with open(out_path, "w") as myfile:

                pdbfile = open(path,"r")
                for line in pdbfile:
                    myfile.write(line)

                pdbfile.close() 

                print("Successfully exported the pdb file to %s" %out_path)

    else:
        print("The directory does not exist ")
