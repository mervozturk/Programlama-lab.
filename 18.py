
import random
class grasspgame(object):
    def __init__(self):
        self.passwins,self.passlosses=0,0
        self.dpwins,self.dplosses,self.dppushes=0,0,0

    def playhand(self):
        throw = rolldie() + rolldie()
        if (throw == 7 or throw == 11):
            self.passwins += 1
            self.dplosses += 1
        elif (throw == 2 or throw == 3 or throw == 12):
            self.passlosses += 1

            if (throw == 12):
                self.dppushes += 1

            else:
                self.dpwins += 1

        else:
            point = throw
            while (True):
                throw = rolldie() + rolldie()
                if (throw == point):
                    self.passwins += 1
                    self.dplosses += 1
                    break
                elif (throw == 7):
                    self.passlosses += 1
                    self.dpwins += 1
                    break

        return self.passwins


def rolldie():
    return random.choice([1,2,3,4,5,6])

def checkpascal(numtri):
    numwins=0
    for i in range(numtri):
        for j in range(24):
            d1 = rolldie()
            d2= rolldie()
            if(d1==6 and d2==6):
                numwins+=1
                break

    print ("sonuc:",numwins/numtri)

checkpascal(100)

c=grasspgame()

for i in range(10):
    c.playhand()
print (c.passwins,"kere kazandın")

