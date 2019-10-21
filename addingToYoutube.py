from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pdb

import pickle

with open("songnames.pkl", "rb") as f:
    songnames = pickle.load(f)

brower = webdriver.Chrome(executable_path = "/Users/shivanshmishra/Documents/GSoC/chromedriver")

website_url = "https://music.youtube.com/"

brower.get(website_url)
input()
for i in range(len(songnames)):
    try:
        WebDriverWait(brower, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon"))).click()
        search = brower.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input")

        to_search = str(songnames[i][0])+" "+songnames[i][1]+" song"
        search.send_keys(to_search)
        search.send_keys(u'\ue007')

        time.sleep(1.5)

       # ActionChains(brower).context_click(brower.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[1]/ytmusic-responsive-list-item-renderer")).perform()
        ActionChains(brower).context_click(WebDriverWait(brower, 20).until(EC.presence_of_element_located((By.XPATH, " /html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[2]/div[1]/ytmusic-responsive-list-item-renderer[1]")))).perform()


        WebDriverWait(brower, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown/div/ytmusic-menu-popup-renderer/paper-listbox/ytmusic-menu-navigation-item-renderer[2]/a"))).click()
        
    #    WebDriverWait(brower, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[2]/div/ytmusic-add-to-playlist-renderer/div[1]/ytmusic-playlist-add-to-option-renderer[1]/button"))).click()
        
        WebDriverWait(brower, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[2]/div/ytmusic-add-to-playlist-renderer/div[1]/ytmusic-playlist-add-to-option-renderer[1]/button"))).click()




    #    /html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[2]/div/ytmusic-add-to-playlist-renderer/div[1]/ytmusic-playlist-add-to-option-renderer[1]/button
    #    /html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[2]/div/ytmusic-add-to-playlist-renderer/div[1]/ytmusic-playlist-add-to-option-renderer[1]/button


        brower.execute_script("window.history.go(-1)")
        time.sleep(2)
    except Exception as e:
        if type(e).__name__ == 'TimeoutException':
            input()
            continue
        brower.refresh()

