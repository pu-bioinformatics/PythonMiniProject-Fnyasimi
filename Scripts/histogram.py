#! /bin/python

"""The module contains the function that is used to produce anini acid histograms
    The module has two function :aminoacid_histogram and count_print."""

def aminoacid_histogram(path):
    
    """This is a fuction used to draw histograms of the number of amino acids present in a sequence of 
    a given pdb file as an input.
    Arguments: path"""
    
    from histogram import count_print

    with open (path, "r") as myfile: # open pdb file
        
        amino_acids = [] #all amino acids present in the chains
        aminoacids_count = {} #number of times each amino acid appears

        for line in myfile:
           
            if line.startswith("SEQRES"):
                sp_line = line.split() #split line
                for amino in sp_line[4:]:
                    if len(amino)==3:
                        amino_acids.append(amino)
                        typec = "amino acids"
                    else:
                        amino_acids.append(amino)
                        typec = "nucleotides"
        
        for amino in amino_acids: #count amino acids
            if amino not in aminoacids_count.keys():
                amino_total = amino_acids.count(amino)
                aminoacids_count[amino]=amino_total
            else:
                pass
        
    print("""
     Choose an option to order by:
        number of %s - ascending   (an)
        number of %s - descending  (dn)
        alphabetically - ascending          (aa)
        alphabetically - descending         (da)"""%(typec,typec))
    
    order = input("""
     order by: """)
    order = order.lower()
    
    print("\n")
    
    if order == 'an' or order == 'dn' or order == 'aa' or order == 'da':

        if order == 'aa': #alphabetically - ascending
            sorted_Key = sorted(aminoacids_count.items()) #keys sorted in ascending order
            aminoacids_count ={}

            for key,value in sorted_Key:
                aminoacids_count[key] = value 
            count_print(aminoacids_count)

        if order == 'da': #alphabetically - descending
            sorted_Key = sorted(aminoacids_count.items(), key = lambda t: t[0])
            sorted_Key.reverse()
            aminoacids_count ={}

            for key,value in sorted_Key:
                aminoacids_count[key] = value
            count_print(aminoacids_count)

        if order == 'an': #number of amino acids - ascending
            sorted_Value = sorted(aminoacids_count.items(), key = lambda t: t[1]) #sort the values only
            aminoacids_count ={}

            for key,value in sorted_Value:
                aminoacids_count[key] = value
            count_print(aminoacids_count)

        if order == 'dn': # number of amino acids - descending
            sorted_Value = sorted(aminoacids_count.items(), key = lambda t: t[1])
            sorted_Value.reverse() # order in descending order
            aminoacids_count ={}

            for key,value in sorted_Value:
                aminoacids_count[key] = value
            count_print(aminoacids_count)
                
    else:
        print("     Invalid option")
        aminoacid_histogram(path)      
        
def count_print(aminoacids_count):
    
    """Print the amino acids count in each protein
    Arguments: a sorted dictionary"""
    
    for amino in aminoacids_count.keys():
        stars = ''
        for i in range(aminoacids_count.get(amino)):
            stars+='*'
        if len(amino) == 2:
            line = "     %s  (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
            print(line)
        else:
            line = "     %s (%3d) : %s" %(amino, int(aminoacids_count.get(amino)), stars)
            print(line)
        