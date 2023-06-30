import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Игнорирует неполную загрузку страницы
    options.page_load_strategy = 'eager'
    # Игнорирует ошибки из Devtools (не приносят пользы в контексте задачи)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()





