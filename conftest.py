from selenium import webdriver
import pytest

# def pytest_addoption(parser):
#     browser =

@pytest.fixture(scope='function')
def driver(request):
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
