from boggle_model import BoggleModel
from boggle_gui import BoggleGUI


class BoggleController:
    """controller of the boggle game connects between the gui and the model"""
    BOARD_SIZE = 4

    def __init__(self) -> None:
        self._gui = BoggleGUI()
        self._model = BoggleModel()

        delete_word_action = self.create_delete_button_action()
        self._gui.set_delete_button_command(delete_word_action)

        new_game_action = self.create_new_game_button_action()
        self._gui.set_new_game_button_command(new_game_action)

        enter_word_action = self.create_enter_word_button_action()
        self._gui.set_enter_word_button_command(enter_word_action)

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                cord = (row, col)
                action = self._create_letter_button_action(cord)
                self._gui.set_letter_command(cord, action)

    def run(self) -> None:
        self._gui.run()

    # function that create the action of the buttons on the board and
    #    connect the gui and the model actions:
    def _create_letter_button_action(self, cord):
        def fun() -> None:
            self._model.do_letter_button(cord)
            current_guessed_word = self._model.get_current_guessed_word()
            self._gui.reload_gui_grid_press(current_guessed_word, cord)
        return fun

    def create_delete_button_action(self):
        def fun():
            self._model.do_delete_button()
            self._gui.reload_gui_delete()
        return fun

    def create_enter_word_button_action(self):
        def fun():
            check_word = self._model.do_enter_word_button()
            self._gui.reload_gui_enter_word(check_word)
        return fun

    def create_new_game_button_action(self):
        def fun():
            new_letters = self._model.do_new_game_button()
            self._gui.reload_gui_new_game(new_letters)
        return fun


if __name__ == "__main__":
    BoggleController().run()