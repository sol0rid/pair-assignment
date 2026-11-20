import Function1 as f1
import Function2 as f2
import function_3 as f3
import function_4 as f4

path = r"C:\Users\annav\OneDrive\project with Rostyslav\pair-assesment\fasta_exampe.fasta"
f1.complement(path)
print(f2.sequence_count(path))
print(f3.sequences_with_start_codon(path))
print(f4.gaps_in_fasta(path))