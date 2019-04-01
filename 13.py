import random

def rolldie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result=""
    for i in range(n):
        result+=str(rolldie())+" "
    print(result)

rollN(5)

def flip(numflips):
    heads=0
    for i in range(numflips):
        if(random.choice(("H","T"))=="H"):
            heads+=1

    return  heads/numflips

print(flip(10))

def flipsim(numflipspertrial,numtrials):
    frachheads=[]
    for i in range(numflipspertrial):
        frachheads.append(flip(numflipspertrial))
        mean = sum(frachheads)/len(frachheads)

    return mean


print (flipsim(10,10))

def fliplot(minexp,maxexp):
    ratios,diffs,xAxis=[],[],[]
    for exp in range(minexp,maxexp+1):
        xAxis.append(2**exp)
    for numflips in xAxis:
        numheads=0
        for n in range(numflips):
            if(random.choice("H","T")=="H"):
                numheads+=1
        numtails=numflips-numheads
        try:
            ratios.append(numheads/numtails)
        except ZeroDivisionError:
            continue
        pylab.title('Difference Between Heads and Tails')
        pylab.xlabel('Number of Flips')
        pylab.ylabel('Abs(#Heads - #Tails)')
        pylab.plot(xAxis, diffs, 'k')
        pylab.figure()
        pylab.title('Heads/Tails Ratios')
        pylab.xlabel('Number of Flips')
        pylab.ylabel('#Heads/#Tails')
        pylab.plot(xAxis, ratios, 'k')
        random.seed(0)
        flipPlot(4, 20)