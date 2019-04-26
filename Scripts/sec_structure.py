#! /bin/python


def secondary_structure(path):
    """The function shows the secondary structure and which amino acids belong to a certain helix
    and the helix ID.
    The function only  works with proteins that are not bound to macromolecules or ligands, 
    works with continuous amino acids in a protein"""
    
    # Create a dictionary with the 3 letter code as key and the ambiguous code as value
    aminoacids_dict = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
                  'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
                  'TYR':'Y','VAL':'V'}

    with open (path, "r") as myfile: # open pdb file

        p_chains = [] #type of chains in the protein
        aa_count = {} #number of amino acids in each chain

        for line in myfile:

            if line.startswith("SEQRES"):

                seq_line = line.split() #split the line into fields 

                chain = seq_line[2] #select the chains from the respective column

                if chain not in p_chains:
                    p_chains.append(chain) #append the chain to the list of chains
                    aa_count[chain]= int(seq_line[3]) #select the count of amino acids in each chain and save to amino acid count

    extension = filename.split(".")
    print("Secondary Structure of PDB id %s" %str.upper(extension[0]))

    for chain in p_chains: #using the list of chains obtained as the iteratable
        aminoacid_seq = [] #initialize a blank amino acid list
        sec_structure = []
        sec_type = [] #initialize secondary structure type and number list

        with open (path, "r") as myfile:
            for line in myfile:

                sp_line = line.split() #split line

                if line.startswith("SEQRES") and chain == sp_line[2]:

                    for amino in sp_line[4:]:
                        if len(amino)==3:
                            amino1_letter = aminoacids_dict.get(amino)
                            aminoacid_seq.append(amino1_letter)
                            sec_structure.append("-")
                            sec_type.append(" ")
                            type = "amino acids:"

                        else:
                            aminoacid_seq.append(amino)
                            type = "nucleotides:"


                if line.startswith("HELIX") and chain == sp_line[4]:
                    #helix_length = sp_line[10]
                    #print(helix_length)
                    helix_sec = []
                    for i in range(int(sp_line[8])-int(sp_line[5])+1):
                        helix_sec.append("/") # create the secondary helix structure

                    #replace the none structure with the helix structure on the specific index
                    sec_structure[int(sp_line[5])-1:int(sp_line[8])] = helix_sec

                    #get the secondary structure ID and insert it on the right index
                    if sp_line[1] == sp_line[2]:
                        structure_id = str(sp_line[2]) 
                        if len(structure_id) == 1:
                            sec_type[int(sp_line[5])-1] = structure_id
                        else:
                            sec_type[int(sp_line[5])-1:int(sp_line[5])+len(structure_id)-1] = structure_id
                    else:
                        structure_id = str(sp_line[2])
                        if len(structure_id) == 1:
                            sec_type[int(sp_line[5])] = structure_id
                        else:
                            sec_type[int(sp_line[5])-1:int(sp_line[5])+len(structure_id)-1] = structure_id

                if line.startswith("SHEET") and chain == sp_line[5]:
                    #sheet_length = sp_line[10]
                    #print(sheet_length)
                    sheet_sec = []
                    for i in range(int(sp_line[9])-int(sp_line[6])+1):
                        sheet_sec.append("|")
                    #print(sec)
                    sec_structure[int(sp_line[6])-1:int(sp_line[9])] = sheet_sec

                    if len(sp_line[2]) > 1:
                        structure_id = str(sp_line[2])
                        if len(structure_id) == 1:
                            sec_type[int(sp_line[6])-1] = structure_id
                        else:
                            sec_type[int(sp_line[6])-1:int(sp_line[6])+len(structure_id)-1] = structure_id
                    else:
                        structure_id = str(sp_line[1]) + str(sp_line[2])
                        if len(structure_id) == 1:
                            sec_type[int(sp_line[6])-1] = structure_id
                        else:
                            sec_type[int(sp_line[6])-1:int(sp_line[6])+len(structure_id)-1] = structure_id


            chain_count = "(" + str(p_chains.count(chain)) + ")"
            length = "(" + str(len(aminoacid_seq)) + ")"

            print("Chain", chain)
            print(chain_count)

            count = 0
            for amino in range(len(aminoacid_seq)+1):
                count+= 1
                if count == 80:
                    aaline = aminoacid_seq[:80]
                    secline = sec_structure[:80]
                    sec_typeline = sec_type[:80]

                    aaline = "".join(aaline)
                    secline = "".join(secline)
                    sctline = "".join(sec_typeline)
                    count = 0

                    print(aaline)
                    print(secline)
                    print(sctline)
                    print("\n")

                    del aminoacid_seq[0:80]
                    del sec_structure[0:80]
                    del sec_type[0:80]

                if len(aminoacid_seq) < 80:
                    aaline = aminoacid_seq[:]
                    secline = sec_structure[:]
                    sec_typeline = sec_type[:]

                    aaline = "".join(aaline)
                    secline = "".join(secline)
                    sctline = "".join(sec_typeline)
                    count = 0

                    print(aaline)
                    print(secline)
                    print(sctline)

                    break

            print(length)
            print("\n")
        