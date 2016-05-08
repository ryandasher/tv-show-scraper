from bs4 import BeautifulSoup
from urllib2 import urlopen

import json
import random
import re

BASE_URL = "https://en.wikipedia.org/wiki/"

def create_show_link(show):
    """
    Takes a TV show name and returns a proper URL.
    """
    # Pretty up the show name input.
    titlecase_show_name = prettify_show_name(show)

    # Slugify our show name, and create our link.
    slugged_show = '_'.join(titlecase_show_name)
    show_link = BASE_URL + 'List_of_%s_episodes' % slugged_show

    return show_link


def get_episodes(show):
    """
    Get our TV episodes.
    """
    # Put together our show URL, hit the URL, and read the contents.
    html = urlopen(create_show_link(show)).read()
    soup = BeautifulSoup(html, 'lxml')

    # Initialize an empty dict, then iterate over our HTML and find cases
    # of the elements we want. Then pull the meaningful text, and also consider
    # an edge case where the text is linked.
    episodes = {}
    season = 1

    for table in soup.findAll('table', 'wikiepisodetable'):
        current_season = "Season " + str(season)
        episodes[current_season] = []
        for td in table.findAll('td', 'summary'):
            if td.string == None:
                episodes[current_season].append(td.a.string)
            else:
                episodes[current_season].append(td.string)
        season += 1

    return episodes


def prettify_show_name(show):
    """
    Make the show name nice and pretty.
    """
    # Split the name of our TV show into a list of words, and capitalize the
    # first word. Create a list of words we do not want to capitalize.
    word_list = re.split(' ', show)
    titlecase_show_name = [word_list[0].capitalize()]
    articles = ['a', 'an', 'of', 'the', 'is', 'and', 'in']

    # Iterate through our list of words and maybe capitalize them.
    for word in word_list[1:]:
        titlecase_show_name.append(word in articles and word or word.capitalize())

    return titlecase_show_name


def return_random_episode(show):
    """
    Give us a random episode from a show we specify
    """
    episodes = get_episodes(show)

    chosen_season = random.choice(list(episodes.keys()))

    episode = random.choice(episodes[chosen_season])

    return episode


def store_episodes(show):
    """
    Store all episodes in a JSON document.
    """
    episodes = get_episodes(show)

    slugged_show = show.replace(' ', '_').replace("'", '')

    try:
        with open(slugged_show + ".json", 'w') as json_file:
            json.dump(episodes, json_file, indent=4)
        return 'Episode document created.'
    except:
        return 'Could not create episode document.'
