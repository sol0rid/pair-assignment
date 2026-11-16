#Function1 to create a complementary strand 

def complement(file_path):
    with open(file_path, "r") as file:
        for f in file: 
            f = f.strip()
            if f.startswith (">"): 
                continue
            else:
                if "U" not in f:
                    complementary_strand = f.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
                    complementary_strand = complementary_strand.upper()
                    print(complementary_strand)
                else: 
                    complementary_RNA_strand = f.replace("A", "u").replace("U", "a").replace("C", "g").replace("G", "c")
                    complementary_RNA_strand = complementary_RNA_strand.upper()
                    print(complementary_RNA_strand)
