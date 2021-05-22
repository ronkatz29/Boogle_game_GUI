from boggle_board_randomizer import randomize_board
from ex12_utils import load_words_dict, is_valid_path


class BoggleModel:
    """ model of the boggle game , contains all the action for the gui"""
    CLEAR_WORD = str()

    def __init__(self) -> None:
        self._current_guessed_word = self.CLEAR_WORD
        self.board = randomize_board()
        self._current_path = list()
        self.word_dict = load_words_dict("boggle_dict.txt")
        self._found_word_dict = dict()

    def do_delete_button(self):
        """
        function called after the delete button has been clicked. the
        function clears the correct word and path of the word
        """
        self._current_guessed_word = self.CLEAR_WORD
        self._current_path = []

    def do_enter_word_button(self):
        """
        function called after the enter_word button has been clicked. the
        function check is the path of the word is fine and if the word
        appears in the words dict
        :return: str of the word if it is fine , else None
        """
        self._current_guessed_word = self.CLEAR_WORD
        word = is_valid_path(self.board, self._current_path, self.word_dict)
        self._current_path = []  # new empty list
        if word not in self._found_word_dict and word is not None:
            self._found_word_dict[word] = True
            return word
        return None

    # start new game with new letters and board
    def do_new_game_button(self):
        """
        :return: the letters of a new board
        """
        self._current_guessed_word = self.CLEAR_WORD
        self._found_word_dict = {}
        self.board = randomize_board()
        return self.board

    def do_letter_button(self, cord):
        """
        function called after a letter clicked on the main board and take
        the cord of the clicked button
        :param cord: Tuple[int,int]
        """
        self._current_guessed_word = self.board[cord[0]][cord[1]]
        self._current_path.append(cord)

    def get_current_guessed_word(self):
        """
        :return: return the the current guessed word
        """
        return self._current_guessed_word

    def _check_same_button_press(self):
        """
        function checks if the same button pressed two times
        """
        for cord in self._current_path:
            if self._current_path.count(cord) > 1:
                return False
        return True
