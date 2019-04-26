#! /bin/python

def pdb_info(path):
    
    """The function is used to display the pdb protein file information including title, chains, number of helices,
    number of sheets and the amino acid sequence of the protein.
    Arguments : the path to the pdb file."""

    global typec
    import textwrap # a module for formating text in python

    # Creating an amino acid dictionary with the 3 letter code as key and the ambiguous code as value
    aminoacids_dict = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
                  'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
                  'TYR':'Y','VAL':'V'}

    with open (path, "r") as myfile: # open pdb file
        
        p_chains = [] # type of chains in the protein
        aa_count = {} # number of amino acids in each chain
        header = "" # initialize the header
        
        for line in myfile: # memory saving mode

            if line.startswith("TITLE"): # If there are no more lines
                head = line.split()
                header = header + " ".join(head[1:])

            if line.startswith("SEQRES"):
                
                seq_line = line.split() #split the line into fields 

                chain = seq_line[2] #select the chains from the respective column

                if chain not in p_chains:
                    p_chains.append(chain) #append the chain to the list of chains
                    aa_count[chain]= int(seq_line[3]) #select the count of amino acids in each chain and save to amino acid count

        # creating the title and formating it
        print("\n")
        main_head = "TITLE"
        prefix = main_head + ": " # add the separator
        preferredWidth = 80 #linewidth from start to end 

        title_wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                           subsequent_indent=' '*len(prefix))

        if len(p_chains) <= 2:
            chains_title = "CHAINS: " + " and ".join(p_chains) #join all the chains together in the subtitle
    
        else:
            chains_title = "CHAINS: " + ", ".join(p_chains[:-1])
            chains_title = chains_title + " and " + "".join(p_chains[-1]) #join all the chains together in the subtitle

        print(title_wrapper.fill(header)) # printing the title
        print(chains_title) #print the chains present
        #print(aa_count)   

    # loop through the protein chains to extract sequence information and secondary structure info
    for chain in p_chains: #using the list of chains obtained as the iteratable
        aminoacid_seq = "" #initialize a blank amino acid string
        helix_count = 0 #initialize helix counter
        sheet_count = 0 #initialize sheet counter

        with open (path, "r") as myfile:
            for line in myfile:
                sp_line = line.split() #split line

                if line.startswith("SEQRES") and chain == sp_line[2]:
                    seq_tag = True #select lines that meet the above conditions

                    for amino in sp_line[4:]:
                        if len(amino)==3:
                            amino1_letter = aminoacids_dict.get(amino)
                            aminoacid_seq = aminoacid_seq + "".join(amino1_letter)
                            typec = "amino acids:"
                        else:
                            aminoacid_seq = aminoacid_seq + "".join(amino) +" "
                            typec = "nucleotides:"

                if line.startswith("HELIX") and chain == sp_line[4]:
                    helix_count += 1

                if line.startswith("SHEET") and chain == sp_line[5]:
                    sheet_count += 1

            # Creating legends
            aminoacids_count ="      Number of "+ typec + (" "*(6-(len(str(aa_count.get(chain)))))) + str(aa_count.get(chain))
            helixcount = "      Number of helix:" + (" "*(len(aminoacids_count) - 22 - len(str(helix_count)))) + str(helix_count)
            sheetcount = "      Number of sheet:" + (" "*(len(aminoacids_count) - 22 - len(str(sheet_count)))) + str(sheet_count)

            #format the sequence paragraph into a wrap
            seqs ="      Sequence"
            prefix = seqs + ": "
            preferredWidth = 66 #lenth of prefix(16) plus preffered width size of amino acid sequence(50 characters)
            seq_wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                           subsequent_indent=' '*len(prefix))

            print(" - "+ "Chain "+ chain)
            print(aminoacids_count)
            print(helixcount)
            print(sheetcount)
            print(seq_wrapper.fill(aminoacid_seq))
