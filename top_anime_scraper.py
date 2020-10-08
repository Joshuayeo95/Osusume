''' Script to scrape the Top X Animes.'''

from bs4 import BeautifulSoup
from datetime import date
import requests
import os.path
import pickle
import time

counter = 0
limit_num = 0
top_animes = {}
num_loops = 100

duplicates = {}
dup_counter = 0

initilize_statement = 'Beep Boop. Initializing Top Anime Scraper ...'
print('=' * len(initilize_statement))
print(initilize_statement)
print('=' * len(initilize_statement))
print()
print(f'Preparing to scrap the Top {num_loops * 50} Animes.')
print()

for pages in range(num_loops):
    url = 'https://myanimelist.net/topanime.php?limit=' + str(limit_num)
        
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    for table_row in soup.find_all('h3', class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3'):
        anime_name = table_row.a.text
        for link in table_row.select('a'):
            anime_url = link['href']

            if anime_name in top_animes.keys():
                duplicates[anime_name] = 'anime_url'
                dup_counter += 1

            top_animes[anime_name] = anime_url

    print(f'Obtaining Urls for the Top {limit_num + 1} to {limit_num + 50} Animes ...')

    counter += 1
    limit_num += 50

print()
print('Beep Boop. Scraping task has been completed.')
print(f'Total number of Anime Urls scraped : {len(top_animes)}')
print(f'Number of potential duplicates : {dup_counter}')
print()

base_file_name = './data/top_animes'
scraping_date = date.today().strftime('%d_%m_%y')
file_name = base_file_name + '_' + scraping_date + '.pickle'

print(f'Saving Top Animes as : {file_name}')
print('Writing to file ...')

with open(file_name, 'wb') as file:
    pickle.dump(top_animes, file)

print('File successfully saved.')
print('Beep Boop. Shutting down ...')
print()
