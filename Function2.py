#Function2 - count how many sequences we have in the FASTA file

def sequence_count(file_path):
    count = 0
    with open(file_path, "r") as file:
        for f in file:
            if f.startswith(">"):
                count +=1
            else: 
                continue
    return count
