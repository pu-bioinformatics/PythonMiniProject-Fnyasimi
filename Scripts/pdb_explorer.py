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
        """

# Start with no pdb file
pdb = "None"

#import all the modules
from menu import menuscreen
from mainframe import mainframe
from filecheck import filecheck
from information import pdb_info
from histogram import aminoacid_histogram
from sec_structure import secondary_structure
from export import pdb_export
from exitloop import exitloop

# Start the program by executing the menuscreen function
menuscreen(pdb)