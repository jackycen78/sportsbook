from utils.sendemail import sendEmail
from content.game import getGameBetContent
from content.player import getPlayerPropsContent
from utils.helper import get_date
from info import sender, receivers


test = True

#playerContent = getPlayerPropsContent(test)
#gameContent = getGameBetContent(test)

#contents = [(f'Player Props {get_date()}', playerContent),
           #(f'Game Props {get_date()}', gameContent),
 #           ]

def send(sub, cont):
    sendEmail(senderInfo=sender, 
              senderName='Betting Odds', 
              receiverAddress=receivers, 
              subject=sub, 
              content=cont)
    
#for sub, cont in contents:
#    send(sub, cont)

def valid_time(txt, minutesBefore=16):

    for t in txt.split(' '):
        time = t[-1]
        if 'h' == time:
            return False
        elif 'm' == time and int(t[:-1]) >= minutesBefore:
            return False
        return True
    
times = ['53s',
            '3m 34s',
            '43m',
            '2h 23m',]

for t in times:
    print(t, valid_time(t))


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