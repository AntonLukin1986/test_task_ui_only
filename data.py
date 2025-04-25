'''Данные для тестирования и локаторы элементов DOM.'''
import os

from selenium.webdriver.common.by import By


class Url:
    '''Доступные страницы.'''
    MAIN = 'https://only.digital/'
    BLOG = MAIN + 'blog'
    COMPANY = MAIN + 'company'
    CONTACTS = MAIN + 'contacts'
    FIELDS = MAIN + 'fields'
    JOB = MAIN + 'job'
    PROJECTS = MAIN + 'projects'
    FORM = PROJECTS + '#brief'


class TestData:
    '''Данные для заполнения анкеты.'''
    NAME = 'Билл'
    EMAIL = 'my@mail.ru'
    PHONE = '+79991234567'
    COMPANY = 'Macrosolid'
    DESCRIPTION = 'Это будет нечто выдающееся!!1'
    FILE_PATH = os.getcwd() + os.sep + 'requirements.txt'


class FormLocators:
    '''Локаторы элементов анкеты.'''
    # Блок "Ваши контакты"
    CONTACTS_TITLE = By.XPATH, '//h3[text()="Ваши контакты"]'
    INPUT_COMPANY = By.XPATH, '//input[@id="company"]'
    INPUT_EMAIL = By.XPATH, '//input[@id="email"]'
    INPUT_NAME = By.XPATH, '//input[@id="name"]'
    INPUT_PHONE = By.XPATH, '//input[@id="phone"]'

    # Блок "О проекте"
    PROJECT_TITLE = By.XPATH, '//h3[contains(text(), "О проекте")]'
    PROJECT_CHECKBOX = By.XPATH, '//input[@type="checkbox"]/..'  # набор
    INPUT_DESCRIPTION = By.XPATH, '//textarea[@id="description"]'

    # Блок "Добавить файл"
    FILE_TITLE = By.XPATH, '//span[text()="Прикрепить файл"]'
    FILE_ATTACH = By.XPATH, '//input[@type="file"]'  # добавить файл

    # Блок "Бюджет"
    BUDGET_TITLE = By.XPATH, '//h3[contains(text(), "Бюджет")]'
    BUDGET_RADIO = By.XPATH, '//input[@name="budget"]/..'  # набор

    # Блок "Откуда вы узнали о нас?"
    RECOMMEND_TITLE = By.XPATH, '//h3[contains(text(), "Откуда вы узнали о нас?")]'
    RECOMMEND_RADIO = By.XPATH, '//input[@name="recommendation"]/..'  # набор

    # Кнопка отправки формы
    SUBMIT_BTN = By.XPATH, '//div[contains(@class, "FormSubmit")]//button[text()="Начать проект"]'


class FooterLocators:
    '''Локаторы элементов футера.'''
    C_D_P_TITLE = By.XPATH, '//footer//span[span]'
    FOOTER = By.XPATH, '//footer'
    FOOTER_YEAR = By.XPATH, '//footer//p[starts-with(text(), "©")]'
    HEADER_BURGER = By.XPATH, '//button[contains(@class, "Header_burger")]'
