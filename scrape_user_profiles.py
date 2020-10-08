## Scraping the Urls of MAL users ##

from scripts import mal_scrapers as mal_scrape
import os.path
import pickle


if os.path.exists('mal_user_profiles.pickle'):
    with open('mal_user_profiles.pickle', 'rb') as file:
        mal_user_profiles = pickle.load(file)
else:
    mal_user_profiles = {}
    with open('mal_user_profiles.pickle', 'wb') as file:
        pickle.dump(mal_user_profiles, file)


if os.path.exists('user_anime_ratings.pickle'):
    with open('user_anime_ratings.pickle', 'rb') as file:
        user_anime_ratings = pickle.load(file)
else:
    user_anime_ratings = {}
    with open('user_anime_ratings.pickle', 'wb') as file:
        pickle.dump(user_anime_ratings, file)    


updated_mal_user_profiles = mal_scrape.mal_user_profiles_scraper(
    mal_user_profiles,
    num_loops=10,
    time_between_loops=30,
    verbose=True
)

path_to_chrome_driver = '/home/yeokoso/Downloads/chromedriver'


updated_user_anime_ratings = mal_scrape.user_completed_animelist_scraper(
    mal_user_profiles,
    user_anime_ratings,
    path_to_chrome_driver,
    browser_loading_buffer=10
)


with open('mal_user_profiles.pickle', 'wb') as file:
    pickle.dump(updated_mal_user_profiles, file)

with open('user_anime_ratings.pickle', 'wb') as file:
    pickle.dump(updated_user_anime_ratings, file)


''' Next Steps:
1. Creating a dictionary of dicts - {Username : {Anime : Score}}
2. Obtaining other Anime Information (Genre / Type / Sequels (maybe self join?)



'''