from Bio import SeqIO

for fasta in SeqIO.parse("test.fasta","fasta"):
    print("\n"+fasta.id)
    print(fasta.seq)