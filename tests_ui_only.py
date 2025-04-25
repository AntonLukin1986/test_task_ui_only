'''Тесты анкеты и футера.'''
from random import choice

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import (
    TestData as td, FormLocators as formloc, FooterLocators as footloc, Url
)


@pytest.fixture(scope='function')
def driver():
    '''Создание драйвера браузера.'''
    options = webdriver.ChromeOptions()
    options.add_argument(argument='start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_submit_button_clickable_if_form_filled(driver):
    '''Кнопка «Начать проект» кликабельна, если форма заполнена.'''
    driver.get(Url.FORM)
    submit_before_is_disabled = driver.find_element(
        *formloc.SUBMIT_BTN
    ).get_property(name='disabled')

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of(
            driver.find_element(*formloc.CONTACTS_TITLE)
        )
    )
    driver.find_element(*formloc.INPUT_NAME).send_keys(td.NAME)
    driver.find_element(*formloc.INPUT_EMAIL).send_keys(td.EMAIL)
    driver.find_element(*formloc.INPUT_PHONE).send_keys(td.PHONE)
    driver.find_element(*formloc.INPUT_COMPANY).send_keys(td.COMPANY)

    driver.execute_script(
        'arguments[0].scrollIntoView()',
        driver.find_element(*formloc.PROJECT_TITLE)
    )
    choice(driver.find_elements(*formloc.PROJECT_CHECKBOX)).click()
    driver.find_element(*formloc.INPUT_DESCRIPTION).send_keys(td.DESCRIPTION)

    driver.execute_script(
        'arguments[0].scrollIntoView()',
        driver.find_element(*formloc.FILE_TITLE)
    )
    driver.find_element(*formloc.FILE_ATTACH).send_keys(td.FILE_PATH)

    driver.execute_script(
        'arguments[0].scrollIntoView()',
        driver.find_element(*formloc.BUDGET_TITLE)
    )
    choice(driver.find_elements(*formloc.BUDGET_RADIO)).click()

    driver.execute_script(
        'arguments[0].scrollIntoView()',
        driver.find_element(*formloc.RECOMMEND_TITLE)
    )
    choice(driver.find_elements(*formloc.RECOMMEND_RADIO)).click()

    input('Проверка капчей...')
    submit_after_is_disabled = driver.find_element(
        *formloc.SUBMIT_BTN
    ).get_property(name='disabled')

    assert submit_before_is_disabled and not submit_after_is_disabled


@pytest.mark.parametrize(
    'page',
    [Url.MAIN, Url.COMPANY, Url.FIELDS, Url.JOB, Url.BLOG, Url.CONTACTS,
     Url.PROJECTS]
)
def test_footer_presents_on_pages(driver, page):
    '''Футер присутствует на всех страницах.'''
    driver.get(page)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of(
            driver.find_element(*footloc.HEADER_BURGER)
        )
    )
    driver.execute_script(
        'arguments[0].scrollIntoView()',
        driver.find_element(*footloc.FOOTER)
    )
    footer_year = driver.find_element(*footloc.FOOTER_YEAR)
    c_d_p_title = driver.find_element(*footloc.C_D_P_TITLE)
    assert footer_year.is_displayed() and c_d_p_title.is_displayed()
