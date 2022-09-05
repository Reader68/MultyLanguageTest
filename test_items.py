#import pytest
#from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    result = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert len(result) != 0, "The 'Add to basket' button is absent!"

