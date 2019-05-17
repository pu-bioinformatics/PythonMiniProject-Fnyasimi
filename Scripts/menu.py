#! bin/python



def menuscreen(pdb):
    
    """
    Creates the main menu look with all the available options which the program can take.
    Prompts the user to select an option from the available options in the Menu."""
    
    #global opt
    
    #Required module
    from mainframe import mainframe
    
    # Main line parts
    a = " PDB FILE ANALYZER "
    b = " Select an option from below:"
    c = "1) Open a PDB File"
    d = "2) Information"
    e = "3) Show histogram of amino acids"
    f = "4) Display Secondary Structure"
    g = "5) Export PDB File"
    h = "6) Exit"
    i = "Current PDB: "

    # creating the lines ensuring they are equal with length 80
    ln1 = ("     "+("*"*80))
    ln2 = ("     "+"*"+a+(" "*(80-len(a)-2))+"*")
    ln3 = ("     "+("*"*80))
    ln4 = ("     "+"*"+b+(" "*(80-len(b)-2))+"*")
    ln5 = ("     "+"*"+(" "*78)+"*")
    ln6 = ("     "+"*"+"     "+c+(" "*(80-len(c)-5-35))+"(O)"+(" "*30)+"*")
    ln7 = ("     "+"*"+"     "+d+(" "*(80-len(d)-5-35))+"(I)"+(" "*30)+"*")
    ln8 = ("     "+"*"+"     "+e+(" "*(80-len(e)-5-35))+"(H)"+(" "*30)+"*")
    ln9 = ("     "+"*"+"     "+f+(" "*(80-len(f)-5-35))+"(S)"+(" "*30)+"*")
    ln10 = ("     "+"*"+"     "+g+(" "*(80-len(g)-5-35))+"(X)"+(" "*30)+"*")
    ln11 = ("     "+"*"+"     "+h+(" "*(80-len(h)-5-35))+"(Q)"+(" "*30)+"*")
    ln12 = ("     "+"*"+(" "*78)+"*")
    ln13 = ("     "+"*"+(" "*(80-len(i)-len(pdb)-3))+i+pdb+" *")
    ln14 = ("     "+("*"*80))
    
    lines = [ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8,ln9,ln10,ln11,ln12,ln13,ln14]
    
    print("\n")
    # Read all lines to recreate menu
    for line in lines:
        print(line)
    
    # prompt user to select an option
    opt = input("     :")
    opt = opt.upper()
    
    # Call the mainframe function which takes in the options and executes them
    mainframe(opt,pdb)
    
