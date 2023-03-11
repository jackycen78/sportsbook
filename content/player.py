from utils.website import Website
from automate.player import PlayerProps
from templates.player import createPlayerEmail
from tests.player import get_all_test_props

def getPlayerPropsContent(test=True):
    if test:
        players = get_all_test_props()

    else:
        site = Website()
        props = PlayerProps(site) 
        players = props.get_all_props()

    return createPlayerEmail(players)