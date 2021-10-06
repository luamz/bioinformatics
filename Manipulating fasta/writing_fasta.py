seq = input("Input sequence:")
file = open("seq.fasta","w")

file.write(">seq\n")
file.write(seq)

file.close()