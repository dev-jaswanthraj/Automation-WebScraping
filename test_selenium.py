from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapxl import get_workbook
from random import randint
import time




def check(item, path):
    try:
        test_data = item.find_element(By.XPATH, path)
        return True
    except:
        return False

def open_browser_with_amazon(name:str):
    option = Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()), options=option) # Driver
    
    driver.get("https://www.amazon.in/")

    elem = driver.find_element(by=By.NAME, value="field-keywords")
    elem.send_keys(name)
    elem.send_keys(Keys.ENTER)

    items = driver.find_elements(By.XPATH, '//div[@data-component-type= "s-search-result"]')

    wb = get_workbook()
    ws = wb.active
    ws['A1'] = "Product Name"
    ws['B1'] = "Product Price"
    #ws['C1'] = "Discount %"
    ws['C1'] = "Image Link"
    for item in items:
        if(check(item=item, path = './/span[@class = "a-size-base-plus a-color-base a-text-normal"]')):
            product_name = item.find_element(By.XPATH, './/span[@class = "a-size-base-plus a-color-base a-text-normal"]').text
        elif(check(item=item, path='.//span[@class = "a-size-medium a-color-base a-text-normal"]')):
            product_name = item.find_element(By.XPATH, './/span[@class = "a-size-medium a-color-base a-text-normal"]').text
        if(check(item=item, path='.//span[@class = "a-price"]')):
            product_price = item.find_element(By.XPATH, './/span[@class = "a-price"]').text
        else:
            product_price = "None"
            #discount = item.find_element(By.TAG_NAME, 'span').text
        if(check(item=item, path=".//img[@class = 's-image']")):
            image_link = item.find_element(By.XPATH, ".//img[@class = 's-image']").get_attribute('src')
        product_info = (product_name, product_price, image_link)
        ws.append(product_info)
   

    filename = name+str(randint(1, 10000))+".xlsx"
    wb.save(filename)
    driver.close()
    return filename


def open_browser_with_flipkart(name:str):
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()), options=option) # Driver
   
    driver.get("https://www.flipkart.com/")
    

    cancel = driver.find_element(By.XPATH,'//button[@class = "_2KpZ6l _2doB4z"]')
    cancel.send_keys(Keys.ENTER)

    search = driver.find_element(By.XPATH, '//input[@name = "q"]')
    search.send_keys(name)
    search.send_keys(Keys.ENTER)

    items = driver.find_elements(By.XPATH, '//div[@class = "_4ddWXP"]')

    print(len(items), items)

    print("Hi")
    


   

#open_browser_with_flipkart("volley Ball")



