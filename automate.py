from bet import * 
import time

def getPlayNowBets(site):

    playnownba = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showmore = '//*[@id="sports-wrapper"]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]/div/div[2]/div/a'
    table = '/html/body/section/section/div[2]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]'

    site.go_to(playnownba)
    site.click(showmore)

    time.sleep(1)
    
    data = site.locate(table).text.split('\n')
    dataLength = 18
    # Remove header
    data = data[5:]

    betsList = []
    numBets = len(data) // dataLength

    
    for i in range(numBets):
        betsList.append(PlayNowBet(data[i * dataLength: (i + 1) * dataLength]))

    for bet in betsList:
        print(bet)