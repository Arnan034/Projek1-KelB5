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
        flm = film.text.split(".",1)
        del flm[0]
        flm[0] = flm[0].replace(")", "")
        flm[0] = flm[0].replace("\n", "*")
        flm[0] = flm[0].replace("(", "*")
        flm = flm[0].split("*", 3)
        print(flm)
        filmList.append(
            {"No": str(i)+".",
            "Gambar": "PhotoTop100Film/"+ str(i) + ".png",
            "Judul": flm[0],
            "Tahun": flm[1],
            "Rating": flm[2],
            }
        )
        i = i+1
    if i > 100: 
        break;

hasil_scraping = open("Top100Film.json", "w")
json.dump(filmList, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()
