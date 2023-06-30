from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.quick_game_page_locators import QuickGamePageLocators as locators
from selenium.webdriver.common.keys import Keys

from utils.sanitize_letter import sanitize_letter


class QuickGamePage(BasePage):
    """
    Класс для работы с формой быстрой игры, наследуется от класса BasePage.
    """
    def play_quick_game(self):
        """
        Метод, который выполняет шаги теста test_quick_game.
        :return: Результат быстрой игры: скорость и кол-во ошибок.
        """
        self.open_quick_game_page()
        self.close_rules()
        self.start_quick_game()
        self.insert_text()
        return self.quick_game_result()

    def play_quick_game_with_errors(self):
        """
        Метод, который выполняет шаги теста test_quick_game_with_errors.
        :return: Результат быстрой игры: скорость и кол-во ошибок.
        """
        self.open_quick_game_page()
        self.close_rules()
        self.start_quick_game()
        self.insert_text_with_errors()
        return self.quick_game_result()

    def open_quick_game_page(self):
        self.element_is_visible(locators.quick_start_btn).click()

    def close_rules(self):
        self.element_is_visible(locators.close_rules_btn).click()

    def start_quick_game(self):
        try:
            self.element_is_visible(locators.game_start_btn).click()
        except TimeoutException:
            pass

    def insert_text(self):
        all_text = self.element_is_visible(locators.all_text, 50).text
        self.element_is_clickable(locators.game_text_input)
        for letter in all_text:
            sanitized_letter = sanitize_letter(letter)
            self.element_is_visible(locators.game_text_input).send_keys(sanitized_letter)

    def check_error(self):
        try:
            self.element_is_visible(locators.game_text_input_error, 0)
            return True
        except TimeoutException:
            return False

    def insert_text_with_errors(self):
        all_text = self.element_is_visible(locators.all_text, 50).text
        self.element_is_clickable(locators.game_text_input)
        for letter in all_text:
            self.element_is_visible(locators.game_text_input).send_keys(letter)
            if self.check_error():
                sanitized_letter = sanitize_letter(letter)
                self.element_is_visible(locators.game_text_input).send_keys(Keys.BACKSPACE)
                self.element_is_visible(locators.game_text_input).send_keys(sanitized_letter)

    def quick_game_result(self):
        speed_result = int(self.element_is_visible(locators.speed_result).text)
        mistakes_result = int(self.element_is_visible(locators.mistakes_result).text)
        return speed_result, mistakes_result
