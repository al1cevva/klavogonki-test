from selenium.webdriver.common.by import By


class QuickGamePageLocators:
    #главная форма сайта
    quick_start_btn = (By.XPATH, '//a[text()="Быстрый старт"]')

    # страница быстрой игры
    close_rules_btn = (By.XPATH, '//div[@id="content"]//input[@value="Закрыть"]')
    game_start_btn = (By.XPATH, '//a[@id="host_start"]')
    game_text_input = (By.XPATH, '//input[@id="inputtext"]')
    game_text_input_error = (By.XPATH, '//input[@class="error"]')
    highlighted_text = (By.XPATH, '//span[@class="highlight"]')
    all_text = (By.XPATH, '//div[@class="full"]/span')

    # результат
    speed_result = (By.XPATH, '//table//div[@class="player you ng-scope"]//div[@class="stats"]/div[2]/span[1]')
    mistakes_result = (By.XPATH, '//table//div[@class="player you ng-scope"]//div[@class="stats"]/div[3]/span[1]')


