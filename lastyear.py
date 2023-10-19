import pandas as pd
import numpy as np
from math import e

names = [
    'Arsenal', 
    'Aston Villa', 
    'Bournemouth', 
    'Brentford', 
    'Brighton', 
    'Chelsea', 
    'Crystal Palace', 
    'Everton', 
    'Fulham',
    'Leeds',  
    'Leicester', 
    'Liverpool', 
    'Man City', 
    'Man United', 
    'Newcastle', 
    "Nott'm Forest",
    'Southampton',
    'Tottenham',
    'West Ham', 
    'Wolves']

teams = pd.DataFrame(names)
teams.columns = ['names']
teams['ELO'] = 1500

#k = 15 for now. test and see how different weighting works
k = 15



matchdata = pd.read_csv("2022stats.csv")
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



