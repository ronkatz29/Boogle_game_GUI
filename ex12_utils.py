import itertools


def load_words_dict(file_path):
    """
    :param file_path: str for file_path of a file that contains the words
                      for the dictionary for the boggle game
    :return: dict , key : str from the file . value: True
    """
    words_dict = dict()
    with open(file_path) as file_data:
        for line in file_data:
            word = line.strip()
            words_dict[word] = True

    return words_dict


def is_valid_path(board, path, words):
    """
    :param board: list of lists each with strings of len 1 or 2
    :param path: list of tuples each represents a coordinate no the board -
                 List[Tuple[int,int]]
    :param words: dict of words - Dict{str: bool}
    :return:function check is the path is legal is yes it returns string for
    legal word else return None for
    """
    word = ""
    if not path:
        return None
    neighbor_cord = path[0]
    for cord in path:
        if not _check_cord_in_board(cord, board):
            return None
        # check is we are not in the first cord:
        if not cord == path[0]:
            if not _check_neighbors(cord, neighbor_cord):
                return None
            neighbor_cord = cord
        word += board[cord[0]][cord[1]]
    if word in words:
        return word


def _check_neighbors(cord, neighbor_cord):
    """
    :param cord: Tuple(int,int)
    :param neighbor_cord: Tuple(int,int)
    :return:True is cords are neighbors else return False
    """
    if max(abs(cord[0] - neighbor_cord[0]), abs(cord[1] - neighbor_cord[1])) \
            > 1:
        return False
    return True


def _check_cord_in_board(cord, board):
    """
    :param board: list of lists each with strings of len 1 or 2
    :param cord: Tuple[int,int]
    :return: True is cord is legal False either
    """
    board_width = len(board[0])
    board_len = len(board)
    if (cord[0] < 0) or (cord[0] > (board_len - 1)):
        return False
    if (cord[1] < 0) or (cord[1] > (board_width - 1)):
        return False
    return True


def find_length_n_words(n, board, words):
    """
    :param n: int len of word between 3 to 16 # לשאול
    :param board: list of lists each with strings of len 1 or 2
    :param words: dict of words - Dict{str: bool}
    :return: List[Tuple[str,List[Tuple[int,int]]]] tuple of str of a words and
             list of the coordinates of the words on the board
    """
    final_list = list()
    board_dict = _board_to_dict(board)
    for word in words:
        word_path = list()
        for key in board_dict:
            if len(key) <= len(word) and key == word[0:len(key)]:
                for cord in board_dict[key]:
                    _find_path_helper(word, board, cord, word_path,
                                      final_list, word[:], n)
    return final_list


def _find_path_helper(word, board, letter_cord, word_cords, final_list,
                      remain_word, len_cord):
    """
    :param word: str for word
    :param board: list of lists each with strings of len 1 or 2
    :param letter_cord: Tuple[int,int]
    :param word_cords: List[Tuple[int,int]]
    :param final_list: List[Tuple[str,List[Tuple[int,int]]]]
    :param remain_word: str
    """
    # Basic conditions:
    if len(word_cords) == len_cord:
        if len(remain_word) == 0:
            x = (word, word_cords[:])
            if x not in final_list:
                final_list.append(x)
        return
    # Fail conditions:
    current_letter = board[letter_cord[0]][letter_cord[1]]
    if len(remain_word) < len(current_letter):
        return
    if current_letter != remain_word[:len(current_letter)]:
        return
    word_cords.append(letter_cord)
    remain_word = remain_word[len(current_letter):]
    neighbors_list = find_neighbors_cord(letter_cord, word_cords, board,
                                         remain_word)
    for neighbor in neighbors_list:
        _find_path_helper(word, board, neighbor, word_cords, final_list,
                          remain_word, len_cord)
    word_cords.pop()


def find_neighbors_cord(cord, visited_cords, board, remain_word):
    """
    :param visited_cords:List[Tuple[int,int]] list of cords we already visited
    :param cord: Tuple[int,int]
    :return: List[Tuple[int,int]]
    """
    # we found the word , just send another recursion with random cord
    if remain_word == "":
        return [(-1, -1)]
    neighbors_list = list()
    for x_move, y_move in itertools.product(range(-1, 2), repeat=2):
        neighbor_cord = cord[0] + x_move, cord[1] + y_move
        if neighbor_cord not in visited_cords and _check_cord_in_board(
                neighbor_cord, board) and neighbor_cord != cord:
            neighbors_list.append(neighbor_cord)
    return neighbors_list


def _board_to_dict(board):
    """
    :param board: list of lists each with strings of len 1 or 2
    :return: Dict(str: Set[Tuple[int,int]]) dict latter of the board as keys
    and the coordinates for value
    """
    board_dict = dict()
    for i in range(len(board)):
        for j in range(len(board[0])):
            letter = board[i][j]
            if letter in board_dict:
                board_dict[letter] += [(i, j)]
            else:
                board_dict[letter] = [(i, j)]
    return board_dict