import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

pd.set_option("display.max_columns", None)

df = pd.read_csv("DataHubseason-1718_csv.csv")

# -------------------------------------------------------------------
# HOW DOES THE REFEREE AFFECT THE OUTCOME OF THE GAME?

uniqueReferees = pd.unique(df.Referee)
hFTRPerRef = []
aFTRPerRef = []
dFTRPerRef = []
totGamesPerRef = []

totalGames = 0

for referee in uniqueReferees:
    hFTRPerRef.append(len(df.loc[((df['Referee'] == referee) & (df['FTR'] == 'H'))]))
    aFTRPerRef.append(len(df.loc[((df['Referee'] == referee) & (df['FTR'] == 'A'))]))
    dFTRPerRef.append(len(df.loc[((df['Referee'] == referee) & (df['FTR'] == 'D'))]))
    totGamesPerRef.append(len(df.loc[(df['Referee'] == referee)]))

refData = {'Referee': uniqueReferees,
           'Home Wins': hFTRPerRef,
           'Away Wins': aFTRPerRef,
           'Draws': dFTRPerRef,
           'Total Games': totGamesPerRef}

dfRef = pd.DataFrame(refData)

#for all games
homeWins = len(df.loc[df['FTR'] == 'H'])
awayWins = len(df.loc[df['FTR'] == 'A'])
draws = len(df.loc[df['FTR'] == 'D'])
allTotalGames = homeWins + awayWins + draws

dfRef.loc[len(dfRef.index)] = ['All Games', homeWins, awayWins, draws, allTotalGames]

dfRef.insert(2, "Home Win %", round(dfRef['Home Wins'] / dfRef["Total Games"], 3))
dfRef.insert(4, "Away Win %", round(dfRef['Away Wins'] / dfRef["Total Games"], 3))
dfRef.insert(6, "Draw %", round(dfRef['Draws'] / dfRef["Total Games"], 3))

dfRef = dfRef.sort_values(by='Total Games')

print(dfRef)

dfRef[['Referee', 'Home Win %', 'Away Win %', 'Draw %']].plot(
    x='Referee',
    kind='barh',
    stacked=True,
    title='Match Outcome Percentage for Each Referee in the EPL (17-18)',
    mark_right=True)
# plt.show()
# ------------------------------------------------------------------------------------------
# HOME GAME RESULT PERCENTAGE BY AVERAGE ATTENDANCE
attendance = pd.read_csv("EPL attendance (17-18) - Sheet1.csv")

attendanceData = {
'Man United': '74976',
'Tottenham': '67953',
'Arsenal': '59323',
'West Ham': '56885',
'Man City': '53812',
'Liverpool': '53049',
'Newcastle': '51992',
'Chelsea': '41282',
'Everton': '38797',
'Leicester': '31583',
'Southampton': '30794',
'Brighton': '30405',
'Stoke': '29280',
'Crystal Palace': '25063',
'West Brom': '24520',
'Huddersfield': '24040',
'Burnley': '20688',
'Swansea': '20623',
'Watford': '20231',
'Bournemouth': '10064'}


df["Home Team Attendance"] = ""

teams = pd.unique(df.HomeTeam)
hWin = []
hLoss = []
hDraw = []
aWin = []
aLoss = []
aDraw = []
hGames = []
aGames = []

for team in teams:
    hWin.append(len(df.loc[((df['HomeTeam'] == team) & (df['FTR'] == 'H'))]))
    hLoss.append(len(df.loc[((df['HomeTeam'] == team) & (df['FTR'] == 'A'))]))
    hDraw.append(len(df.loc[((df['HomeTeam'] == team) & (df['FTR'] == 'D'))]))
    aWin.append(len(df.loc[((df['AwayTeam'] == team) & (df['FTR'] == 'A'))]))
    aLoss.append(len(df.loc[((df['AwayTeam'] == team) & (df['FTR'] == 'H'))]))
    aDraw.append(len(df.loc[((df['AwayTeam'] == team) & (df['FTR'] == 'D'))]))
    hGames.append((len(df.loc[(df['HomeTeam'] == team)])))
    aGames.append((len(df.loc[(df['AwayTeam'] == team)])))

teamData = {'Team': teams,
            'Home Wins': hWin,
            'Home Losses': hLoss,
            'Home Draws': hDraw,
            'Away Wins': aWin,
            'Away Losses': aLoss,
            'Away Draws': aDraw,
            'Home Games': hGames,
            'Away Games': aGames}

dfTeam = pd.DataFrame(teamData)

dfTeam["Average Home Game Attendance"] = ""

homeGameAttendanceIndex = dfTeam.columns.get_loc("Average Home Game Attendance")

print("Team at 0,0:", dfTeam.iat[0,0])
print("attendance: ", attendanceData.get(dfTeam.iat[0,0]))

for x in range(len(dfTeam.index)):
    dfTeam.iat[x, homeGameAttendanceIndex] = attendanceData.get(dfTeam.iat[x, dfTeam.columns.get_loc("Team")])

print(dfTeam)

dfTeam = dfTeam.sort_values(by="Average Home Game Attendance")

print(dfTeam)

dfTeam.insert(2, "Home Win %", round(dfTeam['Home Wins'] / dfTeam["Home Games"], 3))
dfTeam.insert(4, "Home Loss %", round(dfTeam['Home Losses'] / dfTeam["Home Games"], 3))
dfTeam.insert(6, "Home Draw %", round(dfTeam['Home Draws'] / dfTeam["Home Games"], 3))
dfTeam.insert(8, "Away Win %", round(dfTeam['Away Wins'] / dfTeam["Away Games"], 3))
dfTeam.insert(10, "Away Loss %", round(dfTeam['Away Losses'] / dfTeam["Away Games"], 3))
dfTeam.insert(12, "Away Draw %", round(dfTeam['Away Draws'] / dfTeam["Away Games"], 3))

dfTeam[['Team', 'Home Win %', 'Home Loss %', 'Home Draw %']].plot(
    x='Team',
    kind='barh',
    stacked=True,
    title='Home Game Results for Each Teams in the EPL (17-18)',
    mark_right=True)
# plt.show()
# ------------------------------------------------------------------------------------------
#KEY INDICATORS OF SUCCESS

df["HomeCornerDiff"] = df['HC'] - df['AC']
print(df["HomeCornerDiff"])

CornerCatGraph = sns.catplot(x='FTR', y='HomeCornerDiff', data=df)
CornerCatGraph.set(xlabel= "Match Result", ylabel="Home Team Corners - Away Team Corners")

plt.show()

df["HSTDiff"] = df['HST'] - df['AST']
print(df["HSTDiff"])

STCatGraph = sns.catplot(x='FTR', y='HSTDiff', data=df, orient = "v")
STCatGraph.set(xlabel= "Match Result", ylabel="Home Team Shots on Target - Away Team Shots on Target")

plt.show()

df["HSDiff"] = df['HS'] - df['AS']
print(df["HSDiff"])

SCatGraph = sns.catplot(x='FTR', y='HSDiff', data=df)
SCatGraph.set(xlabel= "Match Result", ylabel="Home Team Shots - Away Team Shots")

plt.show()


