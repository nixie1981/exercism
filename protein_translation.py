def proteins(strand):
    trans_table = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan"}
    stops = ["UAA", "UAG", "UGA"]
    result = []
    for i in range (0,len(strand),3):
        codon = strand[i:i+3]
        if codon in stops:
            break
        result.append(trans_table[codon])
        
    return result

