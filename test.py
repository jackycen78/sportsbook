from tests.playertest import getPlayNowTest

bet = getPlayNowTest()[0]

for b in bet:
    b = b.split('\n')
    print(b)
