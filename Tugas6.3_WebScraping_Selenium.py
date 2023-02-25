from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import json
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://m.imdb.com/chart/top/?ref_=nv_mv_250")

filmList = []

i = 1
for film in driver.find_elements(By.CLASS_NAME, "media"):
    print(film.text)
    for img in film.find_elements(By.TAG_NAME,"img"):
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
        flm = film.text.replace(".", "*")
        flm = flm.replace(")", "")
        flm = flm.replace("\n", "*")
        flm = flm.replace("(", "*")
        flm = flm.split("*", 3)
        filmList.append(
            {"No": flm[0]+".",
            "Gambar": "PhotoTop100Film/"+ str(i) + ".png",
            "Judul": flm[1],
            "Tahun": flm[2],
            "Rating": flm[3],
            }
        )
        i = i+1
    if i > 100: 
        break;

hasil_scraping = open("Top100Film.json", "w")
json.dump(filmList, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()
