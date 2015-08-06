# TV episode scraper

Simple scraper that pulls episode data from various TV show season web pages, so long as they follow the traditional HTML table format.

## Setup

After cloning the git repository onto your machine, make a virtual environment (install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) if you don't have it already) for the project and install the requirements with pip:

    $ mkvirtualenv scraper
    $ pip install -r requirements.txt

## Early version

This is a very early demo of what I want this simple application to accomplish. Right now you can just run the program on the command line, and get a random episode from a TV show of your choice. In the end I would like to be able to store episode data in a JSON database so I don't need to hit the website each time I want an episode, and build a front end that goes along with it.

In order to run the program and get a random episode, get into your virtualenvironment, then hop into the Python shell:

    workon scraper
    python

Now run these commands to get a random episode from a TV show of your choice (the example below uses Always Sunny as an example):

    import scraper
    episode = scraper.return_random_episode("it's always sunny in philadelphia")
    episode
