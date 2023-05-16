# https://www.codewars.com/kata/5556282156230d0e5e000089
# 2023-03-07T19:04:38.040+0000
def dna_to_rna(dna):
    return dna.translate(str.maketrans("T", "U"))