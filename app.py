import constants

MAIN_MENU = """
BASKETBALL TEAM STATS TOOL

---- MENU----

Here are your choices:
1) Display Team Stats
2) Quit

Enter an option >"""

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


def show_team_menu():
    """ Prints list of teams with indexes
    Prompts users to choose which teams stats to display
    """
    team_menu_choice = True
    while team_menu_choice:    
        print("\n")
        menu_index = 1
        for team in teams:
            print(f"{menu_index}) {team['team']}")
            menu_index += 1
        try:
            team_menu_choice = int(input("\nEnter an option >"))
            if team_menu_choice > 0 and team_menu_choice <= len(teams):
                show_team_stats(team_menu_choice - 1)
                break
            else:
                raise ValueError()
        except ValueError:
            print("Invalid choice, try again")


def show_team_stats(team_index):   
    team = teams[team_index]
    #team name
    print(f"\nTeam: {team['team']} Stats")
    print("--------------------")
    #total players
    total_players = len(team["players"])
    print(f'Total players: {total_players}')

    total_experienced_players = 0
    total_inexperienced_players = 0
    for player in team["players"]:
        if player['experience'] == True:
            total_experienced_players += 1
        else:
            total_inexperienced_players += 1
    #total experienced players
    print(f'Total experienced: {total_experienced_players}')
    #total inexperienced players
    print(f'Total inexperienced: {total_inexperienced_players}')
    #average height
    total_player_height = 0
    for player in team["players"]:
        total_player_height = total_player_height + player['height']
    average_player_height = round(total_player_height / total_players, 1)
    print(f'Average height: {average_player_height}')
    #List of players
    player_names = [player['name'] for player in team["players"]]
    print("\nPlayers on Team:")
    print("  " + ", ".join(player_names))
    #list of guardians
    list_of_guardians = []
    list_of_list_of_guardians = [player['guardians'] for player in team["players"]]
    for guardians in list_of_list_of_guardians:
        for guardian in guardians:
            list_of_guardians.append(guardian)
    print("\nGuardians:")
    print("  " + ", ".join(list_of_guardians))

    input("\nPress ENTER to continue...")


if __name__ == "__main__":
    
    players = clean_data(constants.PLAYERS)
    teams = balance_teams(constants.TEAMS, players)
 
    main_menu_choice = True
    while main_menu_choice:
        main_menu_choice = input(MAIN_MENU)
        if main_menu_choice == '1':
            show_team_menu()
        elif main_menu_choice == '2':
            main_menu_choice = False
        else: 
            print("You did not make a valid selection")

