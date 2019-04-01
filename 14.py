import random

def createmyhashtable(n):
    mytable=[]
    for i in range(n):
        mytable.append(0)

    return  mytable

def my_hash(size,numbertobeinserted):

    return numbertobeinserted%size


def insertmyhashtable(mytable,numbertobeinserteed):
    iscollision=False
    index=my_hash(len(mytable),numbertobeinserteed)
    if(mytable[index]==0):
        mytable[index] = 1
    else:
        iscollision = True

    return iscollision


dizi=createmyhashtable(11)

def test(size=13,numberofinsert=10):
    mh1 = createmyhashtable(size)
    c=0
    for s in range(numberofinsert) :
        number=random.randint(1,1000)
        if(insertmyhashtable(dizi,number)==True):
            c=c+1
    print(c)

test()

