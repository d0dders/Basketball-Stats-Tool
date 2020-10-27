import constants


def clean_data(source_data):
    return [{
        'name':player.get('name'),
        'guardians':player.get('guardians').split(' and '),
        'experience':player.get('experience') == 'YES',
        'height':int(player.get('height').split()[0])
        } for player in source_data]


if __name__ == "__main__":
    #Anything to be executed goes here
    print(constants.PLAYERS)
    print('---------------------------------------------------------------------')
    #players = [{'name':player.get('name'), 'guardians':player.get('guardians'), 'experience':player.get('experience') == 'YES', 'height':int(player.get('height').split()[0])} for player in constants.PLAYERS]
    players = clean_data(constants.PLAYERS)
    print(players)