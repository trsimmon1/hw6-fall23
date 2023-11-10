import requests
import json
import unittest
import os

###########################################
# Your name:                              #
# Who you worked with:                    #
###########################################

def load_json(filename):
    '''
    Loads a JSON cache from filename if it exists and returns dictionary
    with JSON data or an empty dictionary if the cache does not exist

    Parameters
    ----------
    filename: string
        the name of the cache file to read in

    Returns
    -------
    dict
        if the cache exists, a dict with loaded data
        if the cache does not exist, an empty dict
    '''

    pass

def write_json(filename, dict):
    '''
    Encodes dict into JSON format and writes
    the JSON to filename to save the search results

    Parameters
    ----------
    filename: string
        the name of the file to write a cache to
    
    dict: cache dictionary

    Returns
    -------
    None
        does not return anything
    '''  

    pass

def get_swapi_info(url, params=None):
    '''
    Check whether the 'params' dictionary has been specified. 
    Makes a request to access data with the 'url' and 'params' given, if any. 
    If the request is successful, return a dictionary representation 
    of the decoded JSON. If the search is unsuccessful, print out "Exception!"
    and return None.

    Parameters
    ----------
    url (str): a url that provides information about entities in the Star Wars universe.
    params (dict): optional dictionary of querystring arguments (default value is 'None').
        

    Returns
    -------
    dict: dictionary representation of the decoded JSON.
    '''

    pass

def cache_all_pages(people_url, filename):
    '''
    1. Checks if the page number is found in the dict return by `load_json`
    2. If the page number does not exist in the dictionary, it makes a request (using get_swapi_info)
    3. Add the data to the dictionary (the key is the page number (Ex: page 1) and the value is the results).
    4. Write out the dictionary to a file using write_json.
    
    Parameters
    ----------
    people_url (str): a url that provides information about the 
    characters in the Star Wars universe (https://swapi.dev/api/people).
    
    filename(str): the name of the file to write a cache to 

    Returns
    -------
    None
        does not return anything
    '''

    pass

def get_starships(filename):
    '''
    Access the starships url for each character (if any) from the cache file 
    and pass it to the get_swapi_info function to get data about a person's 
    starship. Do not include characters that don't have starships in the dictionary
    
    Parameter
    ----------
    filename(str): the name of the cache file to read in 
    
    Returns
    -------
    dict: dictionary with the character's name as a key and a list of the name their 
    starships as the value
    '''

    pass

#################### EXTRA CREDIT ######################

def fetch_population_by_species(species_name, species_filename='swapi_species.json'):
    '''
    Using the Star Wars API (SWAPI), create a dictionary that maps each species 
    in the Star Wars universe to the population of their home world.

    1. Use the provided list of species.
    2. For each species, find out their home world.
    3. Fetch the population of each home world.
    4. Return a dictionary where the keys are species names 
    and the values are the respective home world populations.

    Parameters
    ----------
    species_name: string
        the name of the species

    species_filename: string
        filenamne of species cache (default value is 'swapi_species.json')

    Returns
    -------
    dict
        dictionary with name of the species as the key and home world
        population as the value
    '''

    pass


class TestHomework6(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.filename = dir_path + '/' + "swapi_people.json"
        self.cache = load_json(self.filename)
        self.url = "https://swapi.dev/api/people"

    def test_write_json(self):
        write_json(self.filename, self.cache)
        dict1 = load_json(self.filename)
        self.assertEqual(dict1, self.cache)

    def test_get_swapi_info(self):
        people = get_swapi_info(self.url)
        tie_ln = get_swapi_info("https://swapi.dev/api/vehicles", {"search": "tie/ln"})
        self.assertEqual(type(people), dict)
        self.assertEqual(tie_ln['results'][0]["name"], "TIE/LN starfighter")
        self.assertEqual(get_swapi_info("https://swapi.dev/api/pele"), None)
    
    def test_cache_all_pages(self):
        cache_all_pages(self.url, self.filename)
        swapi_people = load_json(self.filename)
        self.assertEqual(type(swapi_people['page 1']), list)
        self.assertEqual(swapi_people['page 1'][0]['name'], 'Luke Skywalker')

    def test_get_starships(self):
        starships = get_starships(self.filename)
        self.assertEqual(len(starships), 19)
        self.assertEqual(type(starships["Luke Skywalker"]), list)
        self.assertEqual(starships['Biggs Darklighter'][0], 'X-wing')

    def test_fetch_population_by_species(self):
        population = fetch_population_by_species()
        self.assertEqual(type(population), dict)
        self.assertEqual(population["Droid"],"Homeworld unknown")
        self.assertEqual(population["Human"],"1000000000000")

    
if __name__ == "__main__":
    unittest.main(verbosity=2)
