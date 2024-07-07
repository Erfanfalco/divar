from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

respon = requests.get("https://divar.ir/s/tehran/buy-apartment/east-tehran-pars?business-type=personal")
htmlfile = respon.text
houses = []
soup = BeautifulSoup(htmlfile, 'html.parser')
anchor = soup.findAll(name='div', class_='post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46')
tels = []

for tag in anchor:
    try:
        houses.append('https://divar.ir' + str(tag.find("a").get("href")))
    except AttributeError:
        pass

for res in houses:
    driver.get(str(res))

    while True:
        try:
            driver.find_element(By.CSS_SELECTOR,
                                'button.kt-button.kt-button--primary.post-actions__get-contact').click()
            break

        except:
            driver.implicitly_wait(3)

    driver.implicitly_wait(3)
    try:
        mobile = driver.find_element(By.NAME, "mobile")
        while True:
            b = input('telephone: ')
            if len(b) == 11:
                break

        mobile.send_keys(b[1:])
        a = input('code: ')
        driver.find_element(By.NAME, "code").send_keys(str(a))
    except:
        pass

    detail = driver.find_elements(By.CSS_SELECTOR, "span.kt-group-row-item__value")
    Details = [item.text for item in detail]
    cost = driver.find_elements(By.CSS_SELECTOR, "p.kt-unexpandable-row__value")
    cost2 = [item.text for item in cost]

    driver.implicitly_wait(3)
    while True:
        try:
            tel = driver.find_element(By.CSS_SELECTOR, "a.kt-unexpandable-row__action.kt-text-truncate").get_property(
                'href')
            break
        except:
            driver.implicitly_wait(3)

    print(f"{tel}, metrazh: {Details[0]}, sakht: {Details[1]}, hazine har metr: {cost2[1]}, tabaghe: {cost2[2]}, emkanat: {Details[3:]}")
