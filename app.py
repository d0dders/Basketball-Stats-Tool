import constants
import sys

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


def show_team_menu(teams):
    """ Prints list of teams with indexes
    Prompts users to choose which teams stats to display
    """
    team_menu_choice = True
    while team_menu_choice:    
        print("\n")
        index = 1
        for team in teams:
            print(f"{index}) {team['team']}")
            index += 1
        try:
            team_menu_choice = int(input("\nEnter an option >"))
            if team_menu_choice > 0 and team_menu_choice <= len(teams):
                team_choice = input("Team Stats")
                show_team_stats(team_menu_choice - 1)
            else:
                raise ValueError()
        except ValueError:
            print("Invalid choice, try again")



if __name__ == "__main__":
    
    players = clean_data(constants.PLAYERS)
    teams = balance_teams(constants.TEAMS, players)
 
    main_menu_choice = True
    while main_menu_choice:
        main_menu_choice = input(MAIN_MENU)
        if main_menu_choice == '1':
            show_team_menu(teams)
        elif main_menu_choice == '2':
            main_menu_choice = False
        else: 
            print("You did not make a valid selection")

