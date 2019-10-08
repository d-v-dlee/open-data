import os
import json

def group_by_event(json_, type_):
    """
    pulls out one specific event type from event_json and 
    returns a list of those specific events.

    inputs
    -----
    json_: json object
    type_: type of event ex ('Shot', 'Pass')
    """
    events = []
    for event in json_:
        event_type = event['type']['name']
        if event_type == type_:
            events.append(event)
    return events

def event_counter(json_, counter):
    """
    takes a json and counts the number of events that happened during that game

    inputs
    ------
    json__: events json
    counter: counter dictionary
    returns
    -----
    counter: counter dict with counts
    """
    for event in json_:
        event_type = event['type']['name']
        counter[event_type] +=1
    return counter

def total_event_counter(json_list, counter, inpath):
    """
    runs through all jsons, and counts the number of events.

    inputs
    ----
    json_list: list of jsons
    counter: counter dict
    inpath: absolute path to jsons
    """
    counter = counter
    for j in json_list:
        try:
            with open(inpath + os.sep + j) as f:
                event_json = json.load(f)
        except:
            with open(inpath + os.sep + j, encoding='utf-8') as f:
                event_json = json.load(f)
        counter = event_counter(event_json, counter)
    return counter


