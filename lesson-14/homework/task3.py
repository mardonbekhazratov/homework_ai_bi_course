import json
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--window-position=-1700,-200")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.demoblaze.com/")

time.sleep(2)

laptops_section = driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'notebook\')"]')
laptops_section.click()

time.sleep(2)

next_page = driver.find_element(By.CSS_SELECTOR, 'button[id="next2"]')
next_page.click()

time.sleep(1)

data = []

count = 0
laptops = driver.find_elements(By.CLASS_NAME, "card-block")
for laptop in laptops:
    count += 1
    name = laptop.find_element(By.CLASS_NAME, "card-title").text
    price = laptop.find_element(By.CSS_SELECTOR,"h5").text
    description = laptop.find_element(By.ID, "article").text
    data.append({
        "name": name,
        "price": price,
        "description": description
    })

current_dir = Path(__file__).resolve().parent
with open(current_dir / "laptops.json","w") as file:
    json.dump(data, file, indent=4)

print(f"Scraped {count} laptops and saved to laptops.json")

time.sleep(3)

driver.quit()