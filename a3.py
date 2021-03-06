"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['GO','NO','ONE'],'NOT')
    False
    """
    return word in wordlist


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['G','O'],['N','O']], 1)
    'NO'
    """
    word = ''
    lst = board[row_index]
    for i in range(len(lst)):
        word = word + lst[i]
        i = i + 1

    return word


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['G','O'],['N','O']],0)
    'GN'
    """

    word = ''

    for i in range(len(board)):
        word = word + board[i][column_index]

    return word
    

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['G','O','N','E'],['B','E','S','T']],'GO')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['G','O','N','E'],['B','E','S','T']],'ET')
    True
    """
    
    for column_index in range(len(board[0])):
            if word in make_str_from_column(board, column_index):
                return True

    return False

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'BOS')
    False
    """

    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('ANT')
    3
    """
    score = 0
    
    if len(word) < 3:
        score = score + 0 * len(word)
    elif len(word) < 7:
        score = score + 1 * len(word)
    elif len(word) < 10:
        score = score + 2 * len(word)
    else: score = score + 3 * len(word)

    return score
        

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    >>> update_score(['Jessica', 3], 'EXCELLENT')
    >>> update_score(['Omar' , 1], 'HI')
    """
    player_info[1] + word_score(word)


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['NS', 'BOS'])
    1
    """
    count = 0
    for word in words:
        if board_contains_word(board, word):
            count = count + 1

    return count
    


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words_list = []
    words = words_file.readlines()

    for word in words:
        word = word.rstrip('\n')
        words_list.append(word)

    return words_list
    

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """

    board= []
    board_row = []
    i = 0

    for row in board_file:
        row = row.rstrip('\n')
        board_row = board_row + row
        board.insert(i,board_row)
        i=i+1
        board_row = []

    return board
