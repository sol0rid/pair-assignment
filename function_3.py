def sequences_with_start_codon(path):
    sequences = {}      
    name = None

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue                    
            if line.startswith(">"):
                name = line[1:]             
                sequences[name] = ""        
            else:
                sequences[name] += line     

    found = []
    for name, seq in sequences.items():
        if "AUG" in seq:
            found.append(name)
    return found