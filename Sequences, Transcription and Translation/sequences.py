from Bio.Seq import Seq

sequence = Seq("ATG")
complement_sequence = sequence.complement()
reverse_complement_sequence = sequence.reverse_complement()


print("Sequence: " + sequence)
print("Complemnt: " + complement_sequence) 
print("Reverse Complement: " + reverse_complement_sequence)