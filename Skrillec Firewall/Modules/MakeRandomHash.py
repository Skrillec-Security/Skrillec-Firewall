import random

class randomz:
    def hashing():
        WeGotOurHas      = 0
        hashing          = ['#','~','!','"','^',')','£','@','a','b','c','d','e','1','f','g','h','i','2','j','k','l','m','n','o','p','q','3','4','r','s','t','u','v','w','x','y','z', '36']
        for x in range(26):
            genRandom = random.randint(1,35)
            GetOurHash = hashing[genRandom]
            WeGotOurHas = f"{WeGotOurHas}{GetOurHash}"
        letHash = WeGotOurHas
        return letHash