import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def group_by_outcome(sub_df):
    shot_dict = {}
    for outcome in sub_df['outcome'].unique():
        outcome_df = sub_df[sub_df['outcome'] == outcome]
        sub_shots = outcome_df['shot_location_start'].values
        shots_x = [x[0] for x in sub_shots]
        shots_y = [x[1] for x in sub_shots]
        shot_dict[outcome] = {'x': shots_x, 'y': shots_y}
    return shot_dict

def team_or_player_shots(shots_df, subject, player=True):
    """
    insert either player or team name to get coordinates of all their shots, 
    their total xG and total goals scored.
    """
    if player:
        col = 'player'
    else:
        col = 'team'
        
    sub_df = shots_df[shots_df[col] == subject]
    shot_dict = group_by_outcome(sub_df)
    
    xg_sum = np.round(sub_df['statsbomb_xg'].sum(), 2)
    actual = sub_df[sub_df['outcome'] == 'Goal'].shape[0]
    
    
    return shot_dict, xg_sum, actual

def visualize_team_or_player_shots(shots_df_viz, subject, player=True):
    """
    pick a player or team to see their chart shot.

    inputs
    ----
    shots_df_viz: dataframe of all shots
    subject: player or country name; str
    player: boolean; default True, set to False to insert team
    """
    shot_dict, xg_sum, actual = team_or_player_shots(shots_df_viz, subject, player)
    
    img1 = mpimg.imread('../../img/field_cropped.jpg')
    fig, ax = plt.subplots(figsize=(10, 8))
    imgplot = plt.imshow(img1)
    ax = plt.gca()
    for k in shot_dict.keys():
        ax.scatter(shot_dict[k]['x'], shot_dict[k]['y'])
    ax.legend(labels=list(shot_dict.keys()))
    ax.text(180, 100, s=f'{subject}\n xG: {xg_sum}\n Goals: {actual}', fontdict={'color': 'black', 'size':12},
       weight='bold')
    ax.set_axis_off()