from utils.helper import get_date
from utils.config import GET_PLAYER, GET_GAME, SEND_EMAIL, TEST_DATA
from utils.sendemail import send_email

from content.game import getGameBetContent
from content.player import getPlayerPropsContent
from tests.player import get_all_test_props
from tests.game import get_all_test_bets

import time

start_time = time.time()

contents = []
if GET_PLAYER:
    if SEND_EMAIL:
        playerContent = getPlayerPropsContent(TEST_DATA)
        contents.append((f'Player Props {get_date()}', playerContent))
    else:
        print(get_all_test_props())
if GET_GAME:
    if SEND_EMAIL:
        gameContent = getGameBetContent(TEST_DATA)
        contents.append((f'Game Props {get_date()}', gameContent))
    else:
        print(get_all_test_bets())

for sub, cont in contents:
   send_email(sub, cont)

print(f'--- Total Time: {round(time.time() - start_time, 2)} ---')
