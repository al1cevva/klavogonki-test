import pytest
from pages.quick_game_page import QuickGamePage


class TestQuickGamePage:
    """
    Класс для тестов быстрой игры.
    """
    def test_quick_game(self, driver):
        form_page = QuickGamePage(driver, 'https://klavogonki.ru/')
        form_page.open()

        result_speed, result_mistakes = form_page.play_quick_game()
        print(f'\nСкорость: {result_speed}зн/мин \nКол-во ошибок: {result_mistakes}')

        assert result_speed >= 400, result_mistakes == 0

    @pytest.mark.skip(reason="Медленный тест, упадет в ошибку")
    def test_quick_game_with_errors(self, driver):
        form_page = QuickGamePage(driver, 'https://klavogonki.ru/')
        form_page.open()

        result_speed, result_mistakes = form_page.play_quick_game_with_errors()
        print(f'\nСкорость: {result_speed}зн/мин \nКол-во ошибок: {result_mistakes}')

        assert result_speed >= 400, result_mistakes == 0
