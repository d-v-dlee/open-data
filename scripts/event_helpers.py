import os
import json
import pandas as pd

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

def total_group_by_event(json_list, type_, inpath):
    """
    runs through JSONs, adds to empty list of events for
    that certain type of dta

    ex. total_group_by_events(json_list, 'Shot', 'somepath')
    """
    total_aggregation = []
    for j in json_list:
        try:
            with open(inpath + os.sep + j, encoding='utf-8') as f:
                event_json = json.load(f)
        except:
            print('unreadable')
        
        events = group_by_event(event_json, type_)
        total_aggregation = total_aggregation + events
    return total_aggregation


############ dataframe creator ##################
def create_shot_dataframe(jsons, inpath, savepath):
    """
    pulls data from shot events and creates a df. that dataframe is then saved and returned

    inputs
    ------
    inpath: string (abs path) to where jsons are stored
    savepath: string (abs path) of where to save created df

    returns
    -----
    shots_df
    """
    
    total_shots = total_group_by_event(jsons, 'Shot', inpath)
    print(f'Total shots: {len(total_shots)}')

    
    #### Pull out of shot data
    # outcome of shots
    shot_outcomes = [shot['shot']['outcome']['name'] for shot in total_shots]
    # foot
    shot_body = [shot['shot']['body_part']['name'] for shot in total_shots]
    # technique
    shot_technique = [shot['shot']['technique']['name'] for shot in total_shots]
    # outcome of shots
    shot_type = [shot['shot']['type']['name'] for shot in total_shots]
    # location of shot
    shot_location_start = [shot['location'] for shot in total_shots]
    # player
    shot_player = [shot['player']['name'] for shot in total_shots]
    # shot teams
    shot_team = [shot['team']['name'] for shot in total_shots]
    # statsbomb xg
    xg = [shot['shot']['statsbomb_xg'] for shot in total_shots]

    shots_df = pd.DataFrame({'outcome': shot_outcomes, 'body_part': shot_body,
             'technique': shot_technique, 'play_type': shot_type,
             'shot_location_start': shot_location_start, 'player': shot_player,
             'statsbomb_xg': xg, 'team': shot_team})
    
    shots_df.to_csv(savepath + os.sep + 'shots_df.csv', index=False)

    return shots_df


########## event counter total #################
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


#######################################