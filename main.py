from utils.helper import get_date
from utils.config import GET_PLAYER, GET_GAME, SEND_EMAIL, TEST_DATA
from utils.sendemail import send_email

from content.game import getGameBetContent
from content.player import getPlayerPropsContent
from tests.player import get_all_test_props
from tests.game import get_all_test_bets


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


'''from utils.website import Website
from joblib import Parallel, delayed
from automate.game import *


def get_all_bets(book):
        book = get_book_class(book)

        book.automate()
        allBets.add_bets(book.bets)
        return allBets
    


def get_book_class(book):
    books = {'Play Now': PlayNow(s1),
             'Pinnacle': Pinnacle(s2),
             'Sports Interact': SportsInteract(s3),
             }
    return books[book]

allBets = AllBets()

s1 = Website()
s2 = Website()
s3 = Website()

Parallel(n_jobs=-1, prefer="threads")(delayed(get_all_bets)(url) for url in ['Play Now', 'Pinnacle', 'Sports Interact'])

print(allBets)'''