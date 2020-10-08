''' Placeholder script for writing and testing functions. '''

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import requests
import random
import pickle
import time

#! Save ranking of anime + date where anime rankings were scraped
#! Get anime name and url to anime page
#! Get review on anime page
#! Sentiment analysis on review
#! Topic modelling

''' Scraping Anime Information'''

url = 'https://myanimelist.net/anime/2904/Code_Geass__Hangyaku_no_Lelouch_R2'

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

anime_metadata = [
    'Type', 'Episodes', 'Status', 'Premiered', 'Producers', 'Licensors', 'Studios', 'Source',
    'Genres', 'Duration', 'Rating', 'Score', 'Ranked', 'Popularity', 'Members', 'Favourites'
]

anime_info = {}

for section in soup.find_all('td', class_='borderClass'):
    for divvy in section.find_all('div'):
        info = divvy.text
        try:
            header, value = info.split(':') 
            print(header)
            if header.strip() in anime_metadata:
                anime_info[header.strip()] = value.strip().replace('\n', '')
        except:
            pass

anime_data = {'Test Anime' : anime_info}

# df = pd.DataFrame.from_dict(anime_data, orient='index')
# print(df.to_string())

anime_name = 'Code_Geass__Hangyaku_no_Lelouch_R2'
anime_dict = {anime_name: anime_info}

df = pd.DataFrame.from_dict(anime_dict, orient='index')
print(df.columns)


''' Data Cleaning 

Type : -
Episodes : Change to int
Status : -
Premiered : season, year = value.split(' ', 1)
Producers : value.strip()
Licensors : value.strip()
Studios : value.strip()







# counter = 0
# limit_num = 0
# top_animes = {}
# num_loops = 100
# 
# duplicates = {}
# dup_counter = 0
# 
# initilize_statement = 'Beep Boop. Initializing Top Anime Scraper ...'
# print('=' * len(initilize_statement))
# print(initilize_statement)
# print('=' * len(initilize_statement))
# print()
# print(f'Preparing to scrap the Top {num_loops * 50} Animes.')
# print()
# 
# for pages in range(num_loops):
    # url = 'https://myanimelist.net/topanime.php?limit=' + str(limit_num)
        # 
    # source = requests.get(url).text
# 
    # soup = BeautifulSoup(source, 'lxml')
# 
    # for table_row in soup.find_all('h3', class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3'):
        # anime_name = table_row.a.text
        # for link in table_row.select('a'):
            # anime_url = link['href']
# 
            # if anime_name in top_animes.keys():
                # duplicates[anime_name] = 'anime_url'
                # dup_counter += 1
# 
            # top_animes[anime_name] = anime_url
# 
    # print(f'Obtaining Urls for the Top {limit_num + 1} to {limit_num + 50} Animes ...')
# 
    # counter += 1
    # limit_num += 50
# 
# print()
# print('Beep Boop. Scraping task has been completed.')
# print(f'Total number of Anime Urls scraped : {len(top_animes)}')
# print(f'Number of potential duplicates : {dup_counter}')
# print()
# 
# 
# 
# 
# for page in range(2):
#     if counter == 0:
#         continue

#     top_anime_url = base_anime_url + f'?limit={limit_num}'




#     counter += 1
#     limit_num += 50








## Scraper for obtaining anime scores from individuals ##

# with open('user_anime_ratings.pickle', 'rb') as f:
#     user_anime_ratings = pickle.load(f)

# print(user_anime_ratings)

# user_anime_ratings = {}

# with open('mal_user_profiles.pickle', 'rb') as f:
#     mal_user_profiles = pickle.load(f)

# path_to_chrome_driver = '/home/yeokoso/Downloads/chromedriver'

# for user, profile_links in mal_user_profiles.items():
#     animelist_url = profile_links[1] # completed anime list
#     browser = webdriver.Chrome(executable_path=path_to_chrome_driver)
#     browser.get(animelist_url)

#     time.sleep(10)
#     soup = BeautifulSoup(browser.page_source, 'lxml')

#     anime_names = []
#     anime_ratings = []

#     for anime_cells in soup.find_all('td', class_='data title clearfix'):
#         anime_names.append(anime_cells.a.text)

#     # Saving anime ratings, which are in String format as there anime without ratings ('-')
#     for anime_rating_cells in soup.find_all('td', class_='data score'):
#         anime_ratings.append((anime_rating_cells.a.span.text.strip()))

#     user_ratings = dict(itertools.zip_longest(anime_names, anime_ratings))
#     user_anime_ratings[user] = user_ratings

#     time.sleep(5)
#     browser.close()

# print(user_anime_ratings)

# counter = 0

# for anime_entry in test_soup.find_all('tr', class_='list-table-data'):
#     print(counter)
#     if counter == 2:
#         break

#     print(anime_entry.contents)

#     counter += 1

    # anime_name_cell = anime_entry.find('td', class_=['data', 'title', 'clearfix'])
    # anime_name = anime_name_cell.a.text

    # anime_score_cell = anime_entry.find('span', class_='score_label')
    # anime_score = anime_score_cell.text

    # print(anime_name + f' : {anime_score}')






Testing how to identify private accounts below.
Verified that only private accounts have the class ownlist_private
'''

# source_1 = requests.get('https://myanimelist.net/animelist/Kyzarou?status=2').text # private
# source_2 = requests.get('https://myanimelist.net/animelist/EverNight?status=2').text # open
# source_3 = requests.get('https://myanimelist.net/animelist/niic?status=2').text # private

# soup_1 = BeautifulSoup(source_1, 'lxml')
# soup_2 = BeautifulSoup(source_2, 'lxml')
# soup_3 = BeautifulSoup(source_3, 'lxml')

# for soup in [soup_1, soup_2, soup_3]:
#     if soup.find('body', class_='ownlist_private'):
#         print('Private Account')
    
#     else:
#         print('Open Account')












