from Bio.Seq import Seq

DNA_sequence = Seq("ATG")
print("\nInitial DNA senquence:", DNA_sequence)

print("\n----- Transcription ----")
mRNA_sequence = DNA_sequence.transcribe()
print("Messenger RNA sequence:", mRNA_sequence)

print("\n----- Back Transcription ----")
print("nDNA sequence:", mRNA_sequence.back_transcribe())

print("\n----- Translation ----")
protein_sequence = mRNA_sequence.translate()
print("Protein sequence from mRNA:", protein_sequence)
protein_sequence = DNA_sequence.translate()
print("Protein sequence from DNA:", protein_sequence)