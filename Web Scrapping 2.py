from selenium import webdriver
import json
from datetime import datetime
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.joox.com/id/chart/36")

top_100 = []
now = datetime.now()
for song in driver.find_elements_by_class_name("SongListItem"):
    for rangking in song.find_elements_by_class_name("SongListCount"):
        print(rangking.text)
    
    for judul in song.find_elements_by_class_name("SongName"):
        print(judul.text)
        
    for penyanyi in song.find_elements_by_class_name("SongDescItem"):
        print(penyanyi.text)
        
    for album in song.find_elements_by_class_name("coverItem"):
        for gambar in album.find_elements_by_tag_name("img"):
            print(gambar.get_attribute("src"))

    
    top_100.append({
        "Rangking" : rangking.text,
        "Judul": judul.text,
        "Penyanyi": penyanyi.text,
        "Album": gambar.get_attribute("src"),
        'Waktu_scrapping':now.strftime("%Y-%m-%d %H:%M:%S")
    })
    

hasil = open("D:\MATKUL POLBAN\SEMESTER 2\PENGEMBANGAN PERANGKAT LUNAK DESKTOP\PRAKTEK\MyResume\WebReka\Top100.json", "w")
json.dump(top_100, hasil, indent = 6)
driver.close()
