import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome(executable_path=r'/home/cuongld/webdriver/chromedriver')
    yield browser
    browser.quit()


