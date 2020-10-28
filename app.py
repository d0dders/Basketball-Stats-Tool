import constants


def clean_data(source_data):
    """ Takes in the PLAYERS constant
    Map the contents of the constant (sorted by experience) into a new dictionary list, cleaning the data as we go.
    Returns the new dictionary list of cleaned and sorted data
    """
    return [{
        'name':player.get('name'),
        'guardians':player.get('guardians').split(' and '),
        'experience':player.get('experience') == 'YES',
        'height':int(player.get('height').split()[0])
        } for player in sorted(source_data, key=lambda k: k['experience'])]

   


def balance_teams(source_teams, players):
    """ Takes list of cleaned and sorted players and the TEAMS constant
    Populates a dictionary with an entry for each team with the team name and an empty players list
    We keep cycling through the teams and step through the players allocating players to team until all players are assigned a team
    Returns the populated teams dictionary
    """
    teams = []
    for team in constants.TEAMS:
        teams.append({'team': team, 'players':[]})
    player_index = 0
    while player_index < len(players):
        for team in teams:
            team["players"].append(players[player_index])
            player_index += 1
    return(teams)


if __name__ == "__main__":
    
    players = clean_data(constants.PLAYERS)
    teams = balance_teams(constants.TEAMS, players)
    for team in teams:
        print(team)
        print("----------------")