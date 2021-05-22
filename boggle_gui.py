import tkinter as tki
from typing import Callable, Any
from functools import partial
from tkinter import messagebox

BUTTON_HOVER_COLOR = 'PaleVioletRed1'
REGULAR_COLOR = 'misty rose'
BUTTON_ACTIVE_COLOR = "light sky blue"

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}

FRAME_BG = "CadetBlue3"
TITLE_BG = "IndianRed1"
SCORE_BG = "aquamarine2"
SCORE_VAL_BG = "lightyellow"
CLOCK_BG = "aquamarine2"
CLOCK_VAL_BG = "lightyellow"
NEW_GAME_BG = "snow"
DELETE_BG = "snow4"
ENTER_WORD_BG = "MediumPurple1"
CURRENT_WORD_BG = "khaki1"
FOUND_WORD_BG = "light salmon"
FOUND_WORD_VAL_BG = "burlywood1"
END_TIME_COLOR1 = "firebrick1"
END_TIME_COLOR2 = "DarkOrange1"
ENTER_MSG_BG = "bisque"
WRONG_GUESS = "IndianRed2"
WRIGHT_GUESS = "SpringGreen3"
ENTER_MASSAGE = "Welcome to Boggle \n\n*-*-GAME " \
           "INSTRUCTION-*-*\n\n" \
           "1 - To start a game press the new game button\n " \
           "2 - To enter a word click the enter word button.\n " \
           "3 - To erase current chosen word and release letter " \
           "buttons\n " \
           "you can click Delete or Enter word button\n " \
           "4 - To start over a word press delete word " \
           "button\n\n" \
           "Your goal is to find as many words as you can\n" \
           "while you " \
           "choose only letters that are neighbors\n\n" \
           "GOOD LUCK MY DEAR FRIEND"
END_TIME_TITLE = "GAME OVER"
ENG_TIME_MASSAGE1 = "Times up buddy :-(\n you scored: "
ENG_TIME_MASSAGE2 = " points!\nif you want to play another game press " \
                    "New Game button"
TITLE = "Boggle by MR KATZ & MR MUSHLION"
HIGH_LIGHT_THICK = 10
FRAME_WIDTH = 40
LABEL_WIDTH_1 = 10
LABEL_WIDTH_2 = 13
LABEL_WIDTH_2_1 = 19
LABEL_WIDTH_3 = 20
LABEL_WIDTH_4 = 40
FONT = ("Courier", 18)
START_TIME = 180
START_GAME_SCORE = 0
CLEAR_LABEL = ""
NEW_BUT_TEXT = '?'


class BoggleGUI:
    """GUI of the Boggle game"""
    _letters = dict()

    def __init__(self) -> None:
        self.pressed_button_lst = set()
        self.is_game_started = False
        self.remaining = START_TIME
        self._num_of_lines = 0
        self.found_word_list = str()
        self._current_letter = str()
        self.root = tki.Tk()
        self.root.title("Boggle")
        self.root.resizable(False, False)
        self.root.geometry("1000x700")
        self._main_window = self.root

        # Set frames and labels on the root:
        self._title = tki.Frame(self.root, bg=FRAME_BG,
                                highlightbackground=FRAME_BG,
                                highlightthickness=HIGH_LIGHT_THICK)

        self._title_label = tki.Label(self._title, font=FONT,
                                      text=TITLE, bg=TITLE_BG, relief="ridge")

        self._score_stopwatch = tki.Frame(self.root, bg=FRAME_BG,
                                          highlightbackground=FRAME_BG,
                                          highlightthickness=HIGH_LIGHT_THICK)

        self._score_title_label = tki.Label(self._score_stopwatch,
                                            font=FONT, text="Score",
                                            bg=SCORE_BG, width=LABEL_WIDTH_1,
                                            relief="ridge")

        self._score_value_label = tki.Label(self._score_stopwatch,
                                            font=FONT,
                                            bg=SCORE_VAL_BG,
                                            width=LABEL_WIDTH_1,
                                            text="0",
                                            relief="ridge")

        self._clock_title_label = tki.Label(self._score_stopwatch,
                                            font=FONT,
                                            bg=CLOCK_BG,
                                            width=LABEL_WIDTH_1, text="Clock",
                                            relief="ridge")

        self._clock_value_label = tki.Label(self._score_stopwatch,
                                            font=FONT,
                                            bg=CLOCK_VAL_BG,
                                            text="--:--",
                                            width=LABEL_WIDTH_3,
                                            relief="ridge")

        self._letters_frame = tki.Frame(self.root, bg=FRAME_BG,
                                        highlightbackground=FRAME_BG,
                                        highlightthickness=HIGH_LIGHT_THICK)
        self._entering_massage_label = tki.Label(self.root,
                                                 relief="ridge", font=FONT,
                                                 bg=ENTER_MSG_BG,
                                                 text=ENTER_MASSAGE)
        self._create_letters_buttons()

        self._control = tki.Frame(self.root, bg=FRAME_BG,
                                  highlightbackground=FRAME_BG,
                                  highlightthickness=HIGH_LIGHT_THICK)

        self._new_game_button = tki.Button(self._control, font=FONT,
                                           text="New Game",
                                           bg=NEW_GAME_BG,
                                           width=LABEL_WIDTH_2,
                                           relief="ridge")

        self._delete_word_button = tki.Button(self._control, font=FONT,
                                              state=tki.DISABLED,
                                              bg=DELETE_BG,
                                              text="Delete Word",
                                              width=LABEL_WIDTH_2,
                                              relief="ridge")

        self._enter_word_button = tki.Button(self._control, font=FONT,
                                             text="Enter Word",
                                             state=tki.DISABLED,
                                             bg=ENTER_WORD_BG,
                                             width=LABEL_WIDTH_2,
                                             relief="ridge")

        self._current_word_label = tki.Label(self._control, font=FONT,
                                             bg=CURRENT_WORD_BG,
                                             width=LABEL_WIDTH_2_1,
                                             relief="ridge")

        self._words = tki.Frame(self.root, bg=FRAME_BG,
                                highlightbackground=FRAME_BG,
                                highlightthickness=HIGH_LIGHT_THICK)

        self._words_found_label = tki.Label(self._words, font=FONT,
                                            text="Words Found",
                                            bg=FOUND_WORD_BG,
                                            width=LABEL_WIDTH_3,
                                            relief="ridge")

        self._found_words_value_label = tki.Label(self._words, font=FONT,
                                                  bg=FOUND_WORD_VAL_BG,
                                                  width=LABEL_WIDTH_4,
                                                  relief="ridge", height=2)

        self._pack_all_root()

    def _pack_all_root(self):
        """
        function pack all the frames and labels that on the root
        """
        self._title.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._title_label.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
        self._score_stopwatch.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._score_title_label.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
        self._score_value_label.pack(side=tki.LEFT, fill=tki.BOTH)
        self._clock_title_label.pack(side=tki.LEFT, fill=tki.BOTH)
        self._clock_value_label.pack(side=tki.LEFT, fill=tki.BOTH, )
        self._letters_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._entering_massage_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._control.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self.under_grid_pack()
        self._letters_frame.pack_forget()

    def under_grid_pack(self):
        """
        puck all the labels and frames that under the grid
        """
        self._new_game_button.pack(side=tki.LEFT, fill=tki.BOTH)
        self._delete_word_button.pack(side=tki.LEFT, fill=tki.BOTH)
        self._enter_word_button.pack(side=tki.LEFT, fill=tki.BOTH)
        self._current_word_label.pack(side=tki.LEFT, fill=tki.BOTH,
                                      expand=True)
        self._words.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._words_found_label.pack(side=tki.LEFT, fill=tki.BOTH)
        self._found_words_value_label.pack(side=tki.LEFT, fill=tki.BOTH,
                                           expand=True)

    def run(self) -> None:
        self._main_window.mainloop()

    def _create_letters_buttons(self) -> None:
        # build the grid
        for i in range(4):
            tki.Grid.columnconfigure(self._letters_frame, i, weight=1)
        for i in range(4):
            tki.Grid.rowconfigure(self._letters_frame, i, weight=1)

        # make the buttons of the grid and put them in the right place
        for row in range(4):
            for col in range(4):
                self._make_letter_for_board(row, col)

    def _make_letter_for_board(self, row, col):
        button = tki.Button(self._letters_frame, text=NEW_BUT_TEXT,
                            **BUTTON_STYLE, state=tki.DISABLED, )
        button.grid(row=row, column=col, sticky=tki.NSEW)
        self._letters[(row, col)] = button

        def _on_enter(event: Any) -> None:
            if not self._letters[(row, col)]["state"] == tki.DISABLED:
                button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            if not self._letters[(row, col)]["state"] == tki.DISABLED:
                button['background'] = REGULAR_COLOR
        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    # set commands for all the buttons
    def set_letter_command(self, cord, cmd: Callable[[], None]):
        self._letters[cord].configure(command=cmd)

    def set_delete_button_command(self, cmd: Callable[[], None]):
        self._delete_word_button.configure(command=partial(cmd))

    def set_enter_word_button_command(self, cmd: Callable[[], None]):
        self._enter_word_button.configure(command=partial(cmd))

    def set_new_game_button_command(self, cmd: Callable[[], None]):
        self._new_game_button.configure(command=partial(cmd))

    def _display_found_words(self, word):
        """
        function display the found word on the found words label
        :param word: str for correct word that found on the list
        """
        num_of_lines = (len(self.found_word_list) + len(word)) // 50
        if num_of_lines > self._num_of_lines:
            self._num_of_lines += 1
            self.found_word_list += "\n"
        self.found_word_list += " " + word
        self._found_words_value_label["text"] = self.found_word_list

    def _display_current_word(self, letter):
        """
        :param letter: str for letter clicked on the board grid
        """
        self._current_word_label.configure(bg=CURRENT_WORD_BG)
        self._current_letter += letter
        self._current_word_label["text"] = self._current_letter

    # reload the gui display is button click and command came from the control
    def reload_gui_grid_press(self, arg, cord):
        self._display_current_word(arg)
        self._letters[cord].configure(state=tki.DISABLED, bg=FRAME_BG)
        self.pressed_button_lst.add(cord)

    def reload_gui_delete(self):
        self._current_word_label.configure(bg=CURRENT_WORD_BG)
        self._current_letter = ""
        self._current_word_label["text"] = self._current_letter
        self._change_buttons_state()

    def reload_gui_enter_word(self, word):
        if word:
            self._update_score(word)
            self._display_found_words(word)
            self._current_word_label.configure(bg=WRIGHT_GUESS)
        else:
            self._current_word_label.configure(bg=WRONG_GUESS)
        self._current_letter = CLEAR_LABEL
        self._change_buttons_state()

    def reload_gui_new_game(self, new_letters):
        self._current_word_label.configure(bg=CURRENT_WORD_BG)
        self._set_clock_and_grid()
        self._current_letter = ""
        self._clear_game_labels()
        self._change_button_state_to_normal(new_letters)

    def _clear_game_labels(self):
        """
        function clears the score and current and found word value label for a
        start of a new game
        """
        self._score_value_label["text"] = START_GAME_SCORE
        self._found_words_value_label["text"] = CLEAR_LABEL
        self._current_word_label["text"] = CLEAR_LABEL
        self.found_word_list = CLEAR_LABEL

    def _change_button_state_to_normal(self, new_letters):
        """
        function put the state of all the buttons to normal after new game
        button has been clicked
        :param new_letters: List[Tuple[int,int]] list of cord
        """
        for key in self._letters:
            letter = new_letters[key[0]][key[1]]
            self._letters[key].config(state=tki.NORMAL, text=letter,
                                      bg=REGULAR_COLOR)
        self._delete_word_button.config(state=tki.NORMAL)
        self._enter_word_button.config(state=tki.NORMAL)

    def _set_clock_and_grid(self):
        """
        function set the clock of the game is the new game button has been
        clicked
        """
        # used for the first call of new game
        if not self.is_game_started:
            self._first_new_game_pack_with_letters()
            self._countdown()
            self.is_game_started = True
        else:
            # check if new game clicked while the time was running or when
            #       the time was up.
            if self.remaining != 0:
                self.remaining = START_TIME
            else:
                self.remaining = START_TIME
                self._countdown()
        self._clock_value_label.configure(bg=CLOCK_VAL_BG)

    def _first_new_game_pack_with_letters(self):
        """
        unpack all the label that come after the grid so we could pack that
        again in order with the grid after the instructions screen is down
        """
        self._entering_massage_label.pack_forget()
        self._control.pack_forget()
        self._new_game_button.pack_forget()
        self._delete_word_button.pack_forget()
        self._enter_word_button.pack_forget()
        self._current_word_label.pack_forget()
        self._words.pack_forget()
        self._words_found_label.pack_forget()
        self._found_words_value_label.pack_forget()
        self._letters_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._control.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self.under_grid_pack()

    def _end_game_action(self):
        """
        function runs if time is up. all buttons except new game disabled
        and a massage is displayed
        """
        for key in self._letters:
            self._letters[key].config(state=tki.DISABLED, text=NEW_BUT_TEXT)
            self._delete_word_button.config(state=tki.DISABLED)
            self._enter_word_button.config(state=tki.DISABLED)
        tki.messagebox.showinfo(END_TIME_TITLE, ENG_TIME_MASSAGE1 +
                                str(self._score_value_label["text"]) +
                                ENG_TIME_MASSAGE2)

    def _change_buttons_state(self):
        """
        change the state to normal to the letters of the grid that have been
        pressed while trying to find a word on the board
        """
        for cord in self.pressed_button_lst:
            self._letters[cord].config(state=tki.NORMAL, bg=REGULAR_COLOR)
        self.pressed_button_lst = set()

    def _update_score(self, word):
        current_score = self._score_value_label["text"]
        self._score_value_label["text"] = str(int(current_score) + (len(
            word)**2))

    def _countdown(self, remaining=None):
        """
        function responsible for the clock of the game, the function is
        called ones in a 1000 millisecond of the main loop and each times
        updated the text of the clock value label.
        :param remaining: int for the remaining time
        """
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 30:
            if self.remaining % 2 == 0:
                self._clock_value_label.configure(bg=END_TIME_COLOR1)
            else:
                self._clock_value_label.configure(bg=END_TIME_COLOR2)

        if self.remaining <= 0:
            self._clock_value_label.configure(text="time's up!")
            self._end_game_action()

        else:
            mins, secs = divmod(self.remaining, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self._clock_value_label.configure(text=timeformat)
            self.remaining = self.remaining - 1
            self.root.after(1000, self._countdown)