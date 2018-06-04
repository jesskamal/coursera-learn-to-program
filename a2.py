def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna1.find(dna2) >= 0

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if dna is a valid sequence that contains
    only 'A', 'T', 'C', or 'G'.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('aTCGGC')
    False
    >>> is_valid_sequence('ATC9GC')
    False
    >>> is_valid_sequence('ATCRTC')
    False
    '''
    num = 0

    for char in dna:
        if char not in 'ATCG':
            num = num + 1

    return num == 0


def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    Return dna sequence obtained by inserting dna2
    into dna1 at the given index.

    Precondition: Index is not greater than string length.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('ATGTCCTG', 'TTCC', 0)
    TTCCATGTCCTG
    >>> insert_sequence('ATGCCC', 'CG', 5)
    ATGCCCCG
    '''

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nuc):

    '''(str) -> str

    Return the complementary nucleotide to nuc.

    Precondition: Nucleotide is only 'A', 'G', 'T', or 'C'.

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    '''

    if nuc == 'A':
        return 'T'
    elif nuc == 'G':
        return 'C'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'C':
        return 'G'


def get_complementary_sequence(dna):

    '''(str) -> str

    Return the dna sequence that is complementary to
    sequence dna.

    Precondition: DNA only includes 'A', 'G', 'T', or 'C'.

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('CC')
    GG
    >>>get_complementary_sequence('ACGTCG')
    TGCAGC
    '''
    new_sequence = ''
    
    for char in dna:
        if char == 'A':
            new_sequence = new_sequence + 'T'
        elif char == 'G':
            new_sequence = new_sequence + 'C'
        elif char == 'T':
            new_sequence = new_sequence + 'A'
        elif char == 'C':
            new_sequence = new_sequence + 'G'

    return new_sequence
    
        
    
