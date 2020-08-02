from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Add couple selenium tests
#1. Submit filled test form
#https://demoqa.com/text-box

def test_form():
    TEST_DATA = {
        'Full_Name': 'test123',
        'Email': 'test123@gmail.com',
        'Current_Address': 'Ukraine, Kyiv',
        'Check': 'Email:test123@gmail.com'
    }

    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "#userName").send_keys(TEST_DATA['Full_Name'])
    driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(TEST_DATA['Email'])
    driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(TEST_DATA['Current_Address'])
    driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys(TEST_DATA['Current_Address'])

    driver.find_element(By.CSS_SELECTOR, "#submit").click()

    assert driver.find_element(By.ID, "email").text == TEST_DATA['Check']

    driver.quit()
test_form()

#2. Click on [Code in it] button after selecting new Category
#https://testpages.herokuapp.com/styled/basic-ajax-test.html

def click_on():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "#combo1").click()

    select = Select(driver.find_element_by_css_selector("#combo1"))
    select.select_by_visible_text("Server")
    time.sleep(4)

    driver.find_element(By.NAME, "submitbutton").click()
    time.sleep(2)
    assert "Processed Form Details" in driver.page_source

    driver.quit()

click_on()

#3. Print all text in Lorem/Ipsum/Dolor columns
#https://the-internet.herokuapp.com/challenging_dom#delete

def all_text():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
    time.sleep(3)

    l_i_d = driver.find_elements_by_css_selector('tbody tr')
    print("--Start--")
    for value in l_i_d:
        print(value .find_element_by_css_selector('td:nth-child(1)').text)
    print("---------")

    for value in l_i_d:
        print(value .find_element_by_css_selector('td:nth-child(2)').text)
    print("---------")
    for value  in l_i_d:
        print(value .find_element_by_css_selector('td:nth-child(3)').text)
    print("---End---")
    driver.quit()

all_text()