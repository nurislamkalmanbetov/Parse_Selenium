from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By # для поиска найти элемент - кнопки
from selenium.webdriver.support.ui import Select # выборка кнопок
import pandas as pd

import time

driver = Chrome("/drivers/chromedriver")

driver.get("https://www.mashina.kg/search/all/")
time.sleep(10)

posts = driver.find_elements(By.CLASS_NAME, "list-item") # elementSSSSSS! All elements!
posts_data = []
for post in posts:
    name = post.find_element(By.CLASS_NAME, 'name')
    price = post.find_element(By.CLASS_NAME, "price").find_element(By.TAG_NAME, "p")
    info = post.find_element(By.CLASS_NAME, "year-miles")
    posts_data.append(
        (name.text,price.text,info.text)
    )
# print(posts_data)
columns = ["Название", "Цена", "Доп инфо"] # описание 
df = pd.DataFrame(posts_data, columns=columns) # для создания списка posts_data- отправляем все списки туда
with pd.ExcelWriter("mashina.xlsx") as writer:
    df.to_excel(writer)

time.sleep(5)
driver.close()