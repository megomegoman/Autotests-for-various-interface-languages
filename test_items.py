import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_search(browser):
    browser.get(link)
    button_basket = None
    try:
        button_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    finally:
        assert button_basket != None, "missing 'add to basket' button"