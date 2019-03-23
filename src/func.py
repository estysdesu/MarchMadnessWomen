

# focus on team wins losses
def winLossCnt(df):
    dfWinLoss = dfTeamNames[["TeamID"]].copy()
    dfWinLoss = dfWinLoss.reindex(columns = ["TeamID","wins","losses"], fill_value=0) # create columns and init w/ 0s
    dfWinLoss = dfWinLoss.rename(columns={"TeamID": "teamId"}) # camelCase

    # find indx of winTeam & loseTeam and add one to their column counts
    for index, row in df.iterrows():
        winTeam = row["WTeamID"]
        loseTeam = row["LTeamID"]
        dfWinLoss.loc[dfWinLoss["teamId"] == winTeam, "wins"] += 1
        dfWinLoss.loc[dfWinLoss["teamId"] == loseTeam, "losses"] += 1

    return dfWinLoss


# create diffVec with team1 - team2 stats
def diffVector(dfStats, dfTeams):

    for index, row in dfTeams.iterrows():
        stats1 = dfStats.loc[dfStats["teamId"] == row["team1"], "wins":]
        stats2 = dfStats.loc[dfStats["teamId"] == row["team2"], "wins":]

        if index == 0:
            diffVec = np.array(stats1) - np.array(stats2)
        else:
            diffVec = np.append(diffVec, np.array(stats1) - np.array(stats2), axis=0)

    return diffVec


# for train data, determine winner & loser of season data: team1 = [1], team2 = [2]
def winTeamVector(dfTourney, dfPred):
    count = 0
    for index, row in dfPred.iterrows():
        test = dfTourney.loc[((dfTourney["WTeamID"] == row["team1"]) & (dfTourney["LTeamID"] == row["team2"]) 
                              | (dfTourney["WTeamID"] == row["team2"]) & (dfTourney["LTeamID"] == row["team1"])), :]

        if len(test) > 0:
            count += 1
            print(count)
            print(row["team1"])
            print(row["team2"])
            print(test)
            print("\n")

    return
