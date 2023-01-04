from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import pandas as pd


start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(start_url)
soup  = bs(page.text,'html.parser')
start_table = soup.find_all('table')
table_rows = start_table[7].find_all('tr')
planet_masses = []
planet_radius = []
planet_names = []



def scrap():
    headers = ['V Mag. (mV)','Proper name','Bayer designation','Distance (ly)','Spectral class','Mass (M☉)','Radius (R☉)','Luminosity (L☉)']
    planet_data = []
    for i in range(0,208):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('td',attrs = {'class','Luminosity'}):
            td_tags = ul_tag.find_all('td')
            temp_list = []
            for index,li_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append('')
            for i in temp_list:
                planet_masses.append(i[8])
                planet_radius.append(i[9])
                planet_distance.append(i[5])
            planet_data.append(temp_list)
            browser.find_element_by_xpath('//*[@id = "primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scraper_2.csv','w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
scrap()

