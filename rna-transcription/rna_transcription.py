def to_rna(dna_strand):
    if not dna_strand:
        return ''

    rna_map = {"G": "C", "C":"G", "T": "A", "A": "U"}
    rna_strand = ""
    for element in dna_strand:
        strand = rna_map[element]
        rna_strand += strand

    return rna_strand
