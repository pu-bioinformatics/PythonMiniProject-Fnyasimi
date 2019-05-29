#! /bin/python

"""The module contains the function that is used to produce anini acid histograms"""

def aminoacid_histogram(path):
    """This is a fuction used to draw histograms of the number of amino acids present in a seqience of 
    a given pdb file as an input."""

    order = input("""
    Choose an option to order by:
        number of amino acids - ascending   (an)
        number of amino acids - descending  (dn)
        alphabetically - ascending          (aa)
        alphabetically - descending         (da)
    order by: """)
    order = order.lower()
    
    print("\n")

    with open (path, "r") as myfile: # open pdb file
        
        amino_acids = [] #all amino acids present in the chains
        aminoacids_count = {} #number of times each amino acid appears

        for line in myfile:
           
            if line.startswith("SEQRES"):
                sp_line = line.split() #split line
                for amino in sp_line[4:]:
                    amino_acids.append(amino)
        
        for amino in amino_acids: #count amino acids
            if amino not in aminoacids_count.keys():
                amino_total = amino_acids.count(amino)
                aminoacids_count[amino]=amino_total
            else:
                pass
        
    if order == 'an' or order == 'dn' or order == 'aa' or order == 'da':

        if order == 'aa': #alphabetically - ascending
            for amino in sorted(aminoacids_count.keys()): #keys sorted in ascending order
                stars = ''
                for i in range(aminoacids_count.get(amino)):
                    stars+='*'
                line = "    %s (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
                print(line)

        if order == 'da': #alphabetically - descending
            sorted_Key = sorted(aminoacids_count.items(), key = lambda t: t[0])
            sorted_Key.reverse()
            aminoacids_count ={}

            for key,value in sorted_Key:
                aminoacids_count[key] = value

            for amino in aminoacids_count.keys():
                stars = ''
                for i in range(aminoacids_count.get(amino)):
                    stars+='*'
                line = "    %s (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
                print(line)

        if order == 'an': #number of amino acids - ascending
            sorted_Value = sorted(aminoacids_count.items(), key = lambda t: t[1]) #sort the values only
            aminoacids_count ={}

            for key,value in sorted_Value:
                aminoacids_count[key] = value

            for amino in aminoacids_count.keys():
                stars = ''
                for i in range(aminoacids_count.get(amino)):
                    stars+='*'
                line = "    %s (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
                print(line)

        if order == 'dn': # number of amino acids - descending
            sorted_Value = sorted(aminoacids_count.items(), key = lambda t: t[1])
            sorted_Value.reverse() # order in descending order
            aminoacids_count ={}

            for key,value in sorted_Value:
                aminoacids_count[key] = value

            for amino in aminoacids_count.keys():
                stars = ''
                for i in range(aminoacids_count.get(amino)):
                    stars+='*'
                line = "    %s (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
                print(line)
                
    else:
        print("Invalid option")
        aminoacid_histogram(path)
        