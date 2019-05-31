#! /bin/python

"""The module contains the function that is used to produce the secondary structure of a pdb file"""

def secondary_structure(path, pdb):
    """The function shows the secondary structure and which amino acids belong to a certain helix
    and the helix ID.
    The function only  works with proteins that are not bound to macromolecules or ligands, 
    works with continuous amino acids in a protein
    Arguments: path - where file is located
               pdb - the loaded pdb file name"""
    
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

        extension = pdb.split(".")
        print("     Secondary Structure of the PDB id %s:" %str.upper(extension[0]))

        for chain in p_chains: #using the list of chains obtained as the iteratable
            aminoacid_seq = [] #initialize a blank amino acid list
            sec_structure = []
            sec_type = [] #initialize secondary structure type and number list

            myfile.seek(0)
            for line in myfile:

                sp_line = line.split() #split line
                if line.startswith("SEQRES") and chain == sp_line[2]:

                    for amino in sp_line[4:]:
                        if len(amino)==3:
                            amino1_letter = aminoacids_dict.get(amino, "X") #if 3 letter code not in dictionary give it X
                            aminoacid_seq.append(amino1_letter)
                            sec_structure.append("-")
                            sec_type.append(" ")
                            type = "amino acids:"

                        else:
                            aminoacid_seq.append(amino)
                            type = "nucleotides:"


                if line.startswith("HELIX") and chain == sp_line[4]:
                    helix_sec = []
                    for i in range(int(line[33:37])-int(line[21:25])+1):
                        helix_sec.append("/") # create the secondary helix structure

                    #replace the none structure with the helix structure on the specific index
                    sec_structure[int(line[21:25])-1:int(line[33:37])] = helix_sec

                    #get the secondary structure ID and insert it on the right index
                    structure_id = str(sp_line[2])
                    if len(structure_id) == 1:
                        sec_type[int(line[21:25])-1] = structure_id
                    else:
                        sec_type[int(line[21:25])-1:int(line[21:25])+len(structure_id)-1] = structure_id

                if line.startswith("SHEET") and chain == sp_line[5]:
                    sheet_sec = []
                    for i in range(int(line[33:37])-int(line[22:26])+1):
                        sheet_sec.append("|")
                    #print(sheet_sec)
                    sec_structure[int(line[22:26])-1:int(line[33:37])] = sheet_sec

                    structure_id = str(sp_line[1]) + str(sp_line[2]) #Strand and sheet ID
                    if len(structure_id) == 1:
                        sec_type[int(line[22:26])-1] = structure_id
                    else:
                        sec_type[int(line[22:26])-1:int(line[22:26])+len(structure_id)-1] = structure_id


            chain_count = "(" + str(p_chains.count(chain)) + ")"
            length = "(" + str(len(aminoacid_seq)) + ")"

            print("     Chain %s:" %chain)
            print("     " + chain_count)

            count = 80
            for i in range(0,len(aminoacid_seq),count):
                print("     " + "".join(aminoacid_seq)[i: i + count] + "\n" + \
                      "     " + "".join(sec_structure)[i: i + count] + "\n" + \
                      "     " + "".join(sec_type)[i: i + count])

                if i == (len(aminoacid_seq)//80)*80:
                    print("     " + length)
                else:
                    print("\n")
            print("\n")
        