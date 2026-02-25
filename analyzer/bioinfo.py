# bioinfo.py - utility functions for sequences

# CODE 1 : Transcription et Translation
def transcription(ADN):
    """Transcrit ADN en ARN (simple mapping used in original code)."""
    sequence = []
    for i in ADN:
        if i == 'T':
            sequence.append('A')
        elif i == 'A':
            sequence.append('U')
        elif i == 'C':
            sequence.append('G')
        elif i == 'G':
            sequence.append('C')
    return ''.join(sequence)

def translation(RNA):
    """Traduit ARN en protéine (traduction codon -> acide aminé)."""
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    protein_sequence = ''
    for i in range(0, len(RNA), 3):
        codon = RNA[i:i+3]
        amino_acid = codon_table.get(codon, '')
        protein_sequence += amino_acid
    return protein_sequence

# CODE 2 : Calcul du pourcentage GC
def calculate_gc_percentage(ADN):
    """Calcule le pourcentage de C/G dans la séquence"""
    nbrCG = 0
    ADN = ADN.upper()
    for i in ADN:
        if i == 'C' or i == 'G':
            nbrCG = nbrCG + 1
    
    if len(ADN) == 0:
        return 0
    
    pourcentageCG = (nbrCG / len(ADN)) * 100
    return round(pourcentageCG, 2)

def validate_sequence(sequence, seq_type):
    """Valide la séquence selon son type (DNA or RNA). Returns (bool, cleaned_sequence_or_error)."""
    sequence = sequence.upper().strip()
    
    if seq_type == 'DNA':
        allowed = set('ATGC')
    else:  # RNA
        allowed = set('AUGC')
    
    if not all(c in allowed for c in sequence):
        return False, f"Séquence invalide. Caractères autorisés pour {seq_type}: {', '.join(sorted(allowed))}"
    
    return True, sequence
