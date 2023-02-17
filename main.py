from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By # для поиска найти элемент - кнопки
from selenium.webdriver.support.ui import Select # выборка кнопок

import time

driver = Chrome("/drivers/chromedriver") # путь к скачанному, и извлеченному хромдрайву в папке

driver.get("https://www.house.kg/")
time.sleep(6)
button = driver.find_element(By.XPATH, "//*[@id='homepage']/header/div/div[2]/ul/li[2]/a[1]")# кнопка зайти в аренду элемент  XPATH
button.click()
time.sleep(6)

# Поиск house.kg
# search = driver.find_element(
#     By.XPATH, '//*[@id="quick-search-fake-form"]/div[1]/input'
#     ) # поисковик элемент  XPATH
# text = input("Введите текст поиска: ")
# search.send_keys(text)
# search.submit() # автоматически enter поисковик     

# type = Select(driver.find_element(By.XPATH, '//*[@id="homepage"]/div[7]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div/select'))
# # поисковик внутри house.kg - кнопка "квартиры"
# type.select_by_value('1') # если есть выборы (options) - то нужно через value

# option = driver.find_element(By.ID, 'bs-select-2-1').click()

title = driver.find_element(By.XPATH, '//*[@id="homepage"]/div[7]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div[1]/p/a')

posts = driver.find_elements(By.CLASS_NAME, 'listing') # 's' главное окно, где пост с полноценным описанием и тд
for post in posts:
    title = post.find_element(By.CLASS_NAME, 'title')
    print(title.text)

time.sleep(6)

driver.close()