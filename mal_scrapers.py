''' Functions for scraping data from MyAnimeList
Author : Joshua Yeo
Last Updated : 11 September 2020
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import random
import pickle
import time

def mal_user_profiles_scraper(mal_user_profiles ,num_loops=10, time_between_loops=30, verbose=True):
    ''' Function that scrapes MyAnimeList for Users and the respective links to their profiles.

    Arguments:
        mal_user_profiles : dict
            Dictionary with MAL Username as key and respective profile links as values.
        num_loops : int
            Number of times to loop the scraper.
        time_between_loops : int
            Time in seconds to wait between 'refreshing' the website.
            Webpage we are scraping from displays recent users, therefore to get new users \
            we need to wait a short period before requesting from the same webpage. 
        verbose : bool
            Displays number of new users added to the dictionary for each loop.
    Returns:
        mal_users_profiles : dict
            Updated list of Usernames and profile links.
    '''

    initial_number_of_users = len(mal_user_profiles)

    loop_counter = 0

    while loop_counter < num_loops:
        initial_users = len(mal_user_profiles)

        source = requests.get('https://myanimelist.net/users.php').text

        soup = BeautifulSoup(source, 'lxml')

        for user_entry in soup.find_all('td', class_='borderClass'):
            user_name = user_entry.div.a.text
            user_profile_url = 'https://myanimelist.net/profile/' + user_name
            user_animelist_url = 'https://myanimelist.net/animelist/' + user_name + '?status=2'
                
            mal_user_profiles[user_name] = [user_profile_url, user_animelist_url]
        
        loop_counter += 1

        new_users_added = len(mal_user_profiles) - initial_users
        
        if verbose:
            print(f'Number of new user profiles added : {new_users_added}')

        time.sleep(time_between_loops)

    total_new_users_added = len(mal_user_profiles) - initial_number_of_users

    print()
    print('Beep Boop. Scraping Finished.')
    print(f'Total number of new users added : {total_new_users_added}')

    return mal_user_profiles


def user_completed_animelist_scraper(mal_user_profiles, user_anime_ratings, chrome_driver_path, browser_loading_buffer=10):
    ''' Function that scrapes the completed animes watched by the user and their respective scores.

    Arguments:
        mal_user_profiles : dict
            Dictionary of usernames and their respective profiles links.
        user_anime_ratings : dict
            Dictionary of users and their the given ratings of their completed anime.
            {username : {anime : rating}}
        chrome_driver_path : str
            Path to chromedriver.
        browser_loading_buffer : int
            Time in seconds to wait for the webpage to finish loading.
    Returns:
        user_anime_ratings : dict
            Updated dictionary of users and their respective anime and ratings.
    '''

    users_updated = 0
    new_users_added = 0

    for user, profile_links in mal_user_profiles.items():
        animelist_url = profile_links[1] # completed anime list
        browser = webdriver.Chrome(executable_path=chrome_driver_path)
        browser.get(animelist_url)

        time.sleep(browser_loading_buffer)
        soup = BeautifulSoup(browser.page_source, 'lxml')

        anime_names = []
        anime_ratings = []

        for anime_cells in soup.find_all('td', class_='data title clearfix'):
            anime_names.append(anime_cells.a.text)

        # Saving anime ratings, which are in String format as there anime without ratings ('-')
        for anime_rating_cells in soup.find_all('td', class_='data score'):
            anime_ratings.append((anime_rating_cells.a.span.text.strip()))

        user_ratings = dict(zip(anime_names, anime_ratings))

        if user_anime_ratings.get(user):
            users_updated += 1
        else:
            new_users_added += 1
        
        user_anime_ratings[user] = user_ratings

        browser.close()

    print()
    print('Beep Boop. Anime Ratings for Users have been updated.')
    print(f'Records updated : {users_updated}')
    print(f'New records added : {new_users_added}')
    print(f'Total number of users : {len(user_anime_ratings)}')
    print()

    return user_anime_ratings