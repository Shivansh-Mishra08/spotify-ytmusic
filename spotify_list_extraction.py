from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
brower = webdriver.Chrome(executable_path = "/Users/shivanshmishra/Documents/GSoC/chromedriver")

website_url = "https://open.spotify.com/playlist/7iVsuduXIAAtxXQa2tidYi?si=j9BfeWLuQk2KGq8L8CIpMQ"

brower.get(website_url)

song_name_artist = []
input()
for i in range(1, 175):
    try:
        data =  str(WebDriverWait(brower,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[4]/div[2]/div[1]/div/div/div[2]/div/section/div/div/div[2]/section/ol/div[{}]/div/li/div[2]/div/div[1]".format(i)))).get_attribute("innerHTML"))
        soup = BeautifulSoup(data)

        data_artist = str(WebDriverWait(brower,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[4]/div[2]/div[1]/div/div/div[2]/div/section/div/div/div[2]/section/ol/div[{}]/div/li/div[2]/div/div[2]".format(i)))).get_attribute("innerHTML"))

        soup_data = BeautifulSoup(data_artist)
        artist_name = soup_data.findAll("a", attrs={'class': 'tracklist-row__artist-name-link'})[0].text
        song_name_artist.append([soup, artist_name])
        time.sleep(0.5)

        print(song_name_artist)
    except:
        continue

print()
print("************")

import pickle

with open ("songnames.pkl", "wb") as f:
    pickle.dump(song_name_artist, f)
