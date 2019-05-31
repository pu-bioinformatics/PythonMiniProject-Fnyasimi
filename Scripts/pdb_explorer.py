#! /bin/python

"""
This script is used to launch the pdb explorer function to enable the user to perform 
functions such as ;
        -Load a pdb file
        -View general information about a pdb file
        -Show the secomdary structure of the protein
        -Show a histogram of the amino acids present
        -Export the pdb file
        -Quit the program
        
Prepared by Festus Nyasimi
"""

# Start with no pdb file
pdb = "None"

#import the  start module
from menu import menuscreen

# Start the program by executing the menuscreen function
menuscreen(pdb)