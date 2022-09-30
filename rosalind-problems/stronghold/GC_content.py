
def readFile(filePath):
    with open(filePath, "r") as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    """GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100 , 6)

# *** Read data from the file (FASTA format)
fastaFILE = readFile("gc_content.txt")
fastaDICT = {}
fastaLabel = ""

for line in fastaFILE:
    if ">" in line:
        fastaLabel = line
        fastaDICT[fastaLabel] = ""
    else:
        fastaDICT[fastaLabel] += line

#Dictionary comprehension
# *** Clean/Prepare the data (format for ease of you with our gc_content function
# *** Format the data (store the data in a convenient way)
# *** Run needed operation on the data (pass the data to our gc_content function)
resultdict = {key: gc_content(value) for (key, value) in fastaDICT.items()}
print(resultdict)
# *** Collect results / rosalind submission format
MaxGCKey = max(resultdict, key=resultdict.get)

print(f'{MaxGCKey[1:]}\n{resultdict[MaxGCKey]}')