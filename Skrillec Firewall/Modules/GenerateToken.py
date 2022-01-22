import random,time,os

token = ""

class Generate:
    def Token():
        global token
        TokenArray   = ['#','~','!','^',')','£','@','a','b','c','d','e','1','f','g','h','i','2','j','k','l','m','n','o','p','q','3','4','r','s','t','u','v','w','x','y','z', '35']
        for x in range (50):
            genRandom = random.randint(1,36)
            MakeToken = TokenArray[genRandom]
            token += MakeToken
        
        with open('Modules\\0qw8ieos\\819iojIWSJdkskj.temp', 'w') as GenToken:
            GenToken.write(token)
        return "Successfully created a token."
