import os
import json
from country_list import countries_for_language


def get_wc_jsons(data_path):
    """
    Function for finding all JSONs in event data that are world cup related.

    inputs
    ----
    data_path: relative path to where events data is stored

    returns
    -----
    wc_jsons: list of json names
    """
    countries = dict(countries_for_language('en'))
    country_names = list(countries.values()) + ['England']
    
    wc_jsons = []
    for r, d, f in os.walk(data_path):
        for f_ in f:
            try:
                with open(data_path + os.sep + f_) as f:
                    event_json = json.load(f)
                    for event in event_json[:2]:
                        team = (event['team']['name'])
                        if team in country_names:
                            wc_jsons.append(f_)
            except:
                with open(data_path + os.sep + f_, encoding='utf-8') as f:
                    event_json = json.load(f)
                    for event in event_json[:2]:
                        team = (event['team']['name'])
                        if team in country_names:
                            wc_jsons.append(f_)
    return wc_jsons
                        