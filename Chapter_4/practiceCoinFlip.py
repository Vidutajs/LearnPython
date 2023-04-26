import random

nrOfStreaks = 0
pattern1 = ['H'] * 6
pattern2 = ['T'] * 6

def genCoinList():
    i = 0
    coinList = []
    while i < 100 :
        coin = ''
        if random.randint(0,1) == 0 :
            coin = 'H'
        else :
            coin = 'T'
        coinList.append(coin)
        i += 1    
    return coinList

def testListForPatterns(coinList):
    e = 0
    for e in range(len(coinList) - 6) :
        if coinList[e:e+6] == pattern1 or coinList[e:e+6] == pattern2 :
            return True
            break


for expNr in range(10000) :
    if testListForPatterns(genCoinList()) :
        nrOfStreaks += 1 


print(str(nrOfStreaks / 100) + '%' )
