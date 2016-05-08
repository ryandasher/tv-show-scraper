# TV episode scraper

Simple scraper that pulls episode data from various TV show season web pages, so long as they follow the traditional HTML table format.

## Setup

After cloning the git repository onto your machine, make a virtual environment (install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) if you don't have it already) for the project and install the requirements with pip:

    $ mkvirtualenv scraper
    $ pip install -r requirements.txt

## Using the Program

In order to run the program and get a show's episodes, get into your virtualenvironment, then hop into the Python shell:

    workon scraper
    python

Now run these commands to get a random episode from a TV show of your choice (the example below uses Always Sunny as an example):

    import scraper
    scraper.return_random_episode("it's always sunny in philadelphia")

Or, if you want to store all episodes in a JSON document, run these commands:

	import scraper
	scraper.store_episodes("it's always sunny in philadelphia")

## Why?

Sometimes I have trouble deciding what episode from a TV series I want to watch, so I want to create some programs that will decide for me.
