import pytest
from selene import browser, be, have


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    """
    Настройка браузера перед каждым тестом
    """
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://google.com'

    yield

    browser.quit()


def test_google_search_qa_guru():
    """
    Тест поиска в Google по запросу 'qa.guru'
    """
    browser.open('/')

    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()

    browser.element('html').should(have.text('About this page'))