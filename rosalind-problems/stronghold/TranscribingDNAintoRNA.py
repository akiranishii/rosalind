def transcription(seq):
    """DNA -> RNA"""
    return seq.replace("T", "U")

print(transcription("GGCCGCTACACCCGCACCCGGACCCAATTGAGCCCCTATGACGAAGAGCCCCGGTACCTGACAAACAACGCCAGGAACAGCAAGATGGTTCTCGTAACACCTACTGCCTTTATTCGCCGAACACCCGGAAACGGAATGTTGGGCCCGAAAAGTGATTCGGAAGCAAGCTGCTTCCTGGGGTTTTCCTTCGATGATCCATCCTCAAAGACGCACCGGACTTGGCAGTGGGTCGCCAATGGGAACTAGTAACTCGTAATAATGCTATCTTTCAACTCGGAAGTAACCACAAAAAAGGAGAAGCCTATCATGCCAAGGTCCGCCACCGTTAACTAACTATAACGACACACCCACGAAAGAATCGCTATAGCCTCTATAGTAGCACCTAGGGAGAGATCCACCACTGCCGCGTCGATCACTGCCAGCACTGCCAAGACCTGTGCGAAAGTATCCTTTCACGCAGCTAGGTGTTTTTCACTCCCAGGCACCGTACCTTTGCGTTTCACTGGTTATTTTTGTAGGTATAAATGAATATAGAACTCAGGTCTAACCGATAGCGTTAATTGGCGTACGGACCAAGTTCGGTCGGAAGCCCTCTCAAGTGCTCAGCGACAAACATGGTCTAACTGTCGAGATCGTACTACTACAAGGCTCGCCTATGACCAGCGTCGACGAGCTGCCATTCGATTCCATTCACTAGCTCTTTACTATTGCAACGCTCAGTACGTTCTAGGCCGACCGAATGCACTTCGAAGGACGAGAATTCTACGTTCGAGTACCAGGTGCATAGAAACGCATAGCGCATCCACTTGATGTATCGCTGAAAATTAGAAACGCTTTGGATAGTCCTAGCCACCTCATGACTCACATTACCCAAGATTTTTCCGACTATTAGAATTACCTTAGTACTAGTATAGGTCGTGAACTTCACTATCCCGGAAGATTTAAAACCGAATGTCGGCTTTCCACAGAACGAGTAGTTAGGT"))