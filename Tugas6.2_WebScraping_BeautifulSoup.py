import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.tvonenews.com/"
page = requests.get(URL) #mengunduh halaman

soup = BeautifulSoup(page.content, "html.parser") #ekstraksi kode html
latest = soup.find(class_="article-list-container") #mengambil article-list-container

title = latest.find_all("h2") #mengambil tag h2
category = latest.find_all("h3") #mengambil tag h3
date = latest.find_all(class_="ali-date content_center") #mengambil kelas ali-date content_center

result = []
for i in range(len(title)):
    result.append({"id":i+1, "judul": title[i].text.strip().replace("\n", ""),
                   "kategori":category[i].text.strip().replace("\n", ""),
                   "tanggal":date[i].text.strip().replace("\n", "")})

hasilJSON = json.dumps(result, indent=2)
JSONFile = open("BeritaTerbaru.json", "w")
JSONFile.write(hasilJSON)
JSONFile.close()


