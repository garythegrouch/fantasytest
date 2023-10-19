import pandas as pd
import numpy as np
from math import e

names = [
    'Arsenal', 
    'Aston Villa', 
    'Bournemouth', 
    'Brentford', 
    'Brighton',
    'Burnley', 
    'Chelsea', 
    'Crystal Palace', 
    'Everton', 
    'Fulham', 
    'Liverpool', 
    'Luton',
    'Man City', 
    'Man United', 
    'Newcastle', 
    "Nott'm Forest", 
    'Sheffield United', 
    'Tottenham',
    'West Ham', 
    'Wolves']

teams = pd.DataFrame(names)
teams.columns = ['names']
teams['ELO'] = 1500

#k = 15 for now. test and see how different weighting works
k = 15

matchdata = pd.read_csv("E0.csv")
matchdata = matchdata[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]


def game(match, teams): 
    hometeam = match['HomeTeam']
    awayteam = match['AwayTeam']
   
    Rhome = teams.loc[teams.names == hometeam, 'ELO']
    Raway = teams.loc[teams.names == awayteam, 'ELO']

    
    delta = Rhome.to_numpy() - Raway.to_numpy()

    if match['FTR'] == 'H': 
        whome = 1
        waway = 0

    elif match['FTR'] == 'A': 
        whome = 0
        waway = 1

    else:
        whome = waway = 0.5

    
    g = goaldifference(abs(match['FTHG'] - match['FTAG']))
    we = expectancy(delta)
    phome = pointsChange(k, g, whome, we)
    paway = pointsChange(k, g, waway, we)

    
    teams.loc[teams.names == hometeam, 'ELO'] = RatingChange(Rhome, phome)
    teams.loc[teams.names == awayteam, 'ELO'] = RatingChange(Raway, paway)  


def goaldifference(difference): 
  g = 3/(1 + e ** (-0.3*difference))

  return g


def RatingChange(Rc, change):
   return Rc + change

def pointsChange(k, g, w, we): 
  p = k*g*(w - we)
  
  return p

def expectancy(ratingdiff): 
  we = 1/(10 ** (-ratingdiff/400) + 1)
  
  return we

for i in range(0, len(matchdata)):
  game(matchdata.loc[i], teams)


teams = teams.sort_values('ELO', ascending = False)
print(teams)

#print(teams.names)







# weeksgames = pd.read_csv('odds3.csv')

# gamesthisweek = pd.DataFrame()
# gamesthisweek['home'] = weeksgames['teamathome']
# gamesthisweek['away'] = weeksgames['teamaway']



# def match(game, teams): 
#   weekhometeam = game['teamathome']
#   print(teams.loc[teams.names == weekhometeam, 'ELO'])
   

# for i in range(0, len(weeksgames)): 
#     #print(type(match(weeksgames.loc[i], teams)))
    
    
    
#     #weeksgames['hometeamELO'] = match(weeksgames.loc[i], teams)
#     1 + 1 
#     #gamesthisweek['homeELO'] = 
#     match(weeksgames.loc[i], teams)
#     #gamesthisweek['awayELO'] = match(weeksgames.loc[i], teams)
#     #weeksgames['hometeamELO'] = match(weeksgames.loc[i], teams)
#     #weeksgames.hometeamELO = weeksgames.hometeamELO.astype(np.int64())
#     #print(type(weeksgames.hometeamELO))
#     #print(weeksgames.loc[i])










# #print(type(weeksgames.hometeamELO))
# print(gamesthisweek)

# # hometeams = set(weeksgames['hometeams'])
# # #print(hometeams)
# # teams['ELO'] = teams['ELO'].astype(object)

# # weeksgames = weeksgames.merge(teams, how = 'left', left_on = 'hometeam', right_on = 'ELO')
# # weeksgames.ELO = weeksgames.ELO.notnull().astype(int)

# # weeksgames[hometeamELO] = 

# #print(weeksgames)
# #weeksgames['hometeamELO'] = teams.loc[weeksgames.iloc.hometeam.eq(teams.iloc.names), 'ELO']

# #print(weeksgames.iloc[0].hometeam == teams.iloc[13].names)



 