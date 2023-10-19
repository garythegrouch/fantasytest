from elo_ratings import teams
import pandas as pd
import numpy as np 

odds = pd.read_csv('odds3.csv')

#print(odds.columns)
#odds['hometeamELO'] = teams.loc[teams.names == odds.hometeam, 'ELO']
odds['hometeamELO'] = 0
#odds['hometeam'] = odds.hometeam.astype(str)
odds['hometeamELO'] = teams.loc[odds['hometeam'].isin(teams['names']), 'ELO']




odds.merge(teams, how = 'inner')
# odds['awayteamELO'] = teams.loc[teams.names.eq(odds.awayteam), 'ELO']
#print(teams.names)
print(odds)
#odds.loc[odds.hometeam == 'Chelsea', 'hometeamELO'] = 88
# with pd.option_context('display.max_columns', None):
#     print(odds)

#print(teams)


