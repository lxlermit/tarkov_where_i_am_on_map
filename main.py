import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

dir = r'C:\Users\Chiter\Documents\Escape from Tarkov\Screenshots'
extension_file = 'png'

# href_map = 'https://альп-спб.рф/admin.html'
href_map = 'https://tarkov-market.com/maps/ground-zero'


def check_file(dir, extension_file):
    list_files_in_path = os.listdir(dir)
    print(f'list_files_in_path = {list_files_in_path}')
    num = len(extension_file)
    for file in list_files_in_path:
        extension = file[-num:]
        if extension_file == extension:
            print(f'YRA')
            file_name = file
            return file_name
    return False

def work_with_input(filename, href_map):
    browser = webdriver.Chrome()

    browser.get(href_map)
    time.sleep(2)
    elem_button = browser.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div/div[2]/div/div/div[1]/div[2]/button')
    elem_button.click()
    time.sleep(3)
    elem_input = browser.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div/div[2]/div/div/div[1]/div[2]/input')
    elem_input.send_keys(filename)
    #
    # elem_button = browser.find_element(by=By.XPATH, value='/html/body/center/form/input[1]')
    # elem_button.send_keys("Hi, Vova")
    # time.sleep(2)
    # elem_input = browser.find_element(by=By.XPATH, value='/html/body/center/form/input[2]')
    # elem_input.send_keys("Hi, Vova")






    time.sleep(15)

    # elem = WebDriverWait(browser, 10, 1).until(
    #     expect.visibility_of_element_located(
    #         (By.XPATH, "//input[@placeholder='Search in your collabs']")))
    # elem.send_keys("Text you want to send")

def main():
    while True:
        time.sleep(2)
        file_name = check_file(dir=dir, extension_file=extension_file)
        if file_name:
            print(f'file_name = {file_name}')
            work_with_input(filename=file_name, href_map=href_map)

            time.sleep(5)
            break



if __name__ == '__main__':
    main()
