#! /bin/python

"""The module contains the function used to extract the pdb information from a pdb file"""

def pdb_info(path,pdb):
    
    """The function is used to display the pdb protein file information including title, chains, number of helices,
    number of sheets and the amino acid sequence of the protein.
    Arguments : the path to the pdb file."""

    global typec # distinguish between amino acids and nucleotides

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
        print("     PDB File: %s"%pdb)
        main_head = "     Title: "
        titlelist = []
        len_main_head = len(main_head)
        for i in range(0,len(header),74):
            ln =(" "*len_main_head) + header[i:i+74]
            titlelist.append(ln)

        line1 = titlelist[0]
        line1 = list(line1)
        line1[0:len_main_head]=main_head
        line1 = "".join(line1)
        titlelist[0] = line1
        for line in titlelist:
            print(line)
        
        if len(p_chains) <= 2:
            chains_title = "     CHAINS: " + " and ".join(p_chains) #join all the chains together in the subtitle

        else:
            chains_title = "     CHAINS: " + ", ".join(p_chains[:-1])
            chains_title = chains_title + " and " + "".join(p_chains[-1]) #join all the chains together in the subtitle

        print(chains_title) #print the chains present
        
        # loop through the protein chains to extract sequence information and secondary structure info
        for chain in p_chains: #using the list of chains obtained as the iteratable
            aminoacid_seq = "" #initialize a blank amino acid string
            helix_count = 0 #initialize helix counter
            sheet_count = 0 #initialize sheet counter
            myfile.seek(0)
            
            for line in myfile:
                sp_line = line.split() #split line

                if line.startswith("SEQRES") and chain == sp_line[2]:
                    seq_tag = True #select lines that meet the above conditions

                    for amino in sp_line[4:]:
                        if len(amino)==3:
                            amino1_letter = aminoacids_dict.get(amino, "X") #if amino acid not in dictionary put X
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
            aminoacids_count ="      Number of "+ typec + "%6d" %int(aa_count.get(chain))
            helixcount = "      Number of helix:" + "%12d" %int(helix_count)
            sheetcount = "      Number of sheet:" + "%12d" %int(sheet_count)

            #format the sequence paragraph split the lines to the length of 50
            linelist = []
            s_title = "      Sequence:  "
            len_s_title = len(s_title)
            for i in range(0,len(aminoacid_seq),50):
                ln = (" "*len_s_title)+ aminoacid_seq[i:i+50]
                linelist.append(ln)

            line1 = linelist[0] #select line 1 from list
            line1 = list(line1) # cast it as list
            line1[0:len_s_title]=s_title #add sequence title
            line1 = "".join(line1) #join it
            linelist[0] = line1 #add it back to the list

            print("      - "+ "Chain "+ chain)
            print("   " + aminoacids_count)
            print("   " + helixcount)
            print("   " + sheetcount)
            for line in linelist:
                print("   " + line)
