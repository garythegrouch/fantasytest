import pandas as pd 


teams = pd.read_csv("()_season data.csv")
teams = teams[['team', 'matches', 'wins', 'draws', 'conceded', 'xGA', 'xGA_diff', 'deep_allowed' ]]

column_names = list(teams.columns.values)


def calculate_defense(team): 
    return 0


for team in teams: 
    calculate_defense(team)



print(teams)






