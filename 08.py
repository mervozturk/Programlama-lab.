
print("1. soru")
def carpan(x):
    liste=[]
    for i in range(2,int(x/2)+1):
            while(x%i==0):
                x=x/i
                liste.append(i)

    return liste


    return liste
def asal_bul(x):
    if(a%2==0):
         print(a,"asal degildir")
         print("carpan=",carpan(x))

    else:
        for i in range(3,a//2,2):
            if(a%i==0):
                print(a,"asal degildir:")
                print("carpan", carpan(x))
                break
        else:
             print(a,"asaldır")


a=int(input("bir sayı giriniz:"))
asal_bul(a)

print("2. soru")
liste=[4,-3,2,-1,-2,6,-5]
def sayi(list):
    n=len(list)+1
    max=0

    for i in range(2,n):
        for j in range(0,(n-i)):
            top=0
            a=0
            while(a!=(i-1)):
                top=top+list[j+a]
                a=a+1
            if(top>max):
                max=top
    return max
print("En buyuk toplam: ",sayi(liste))


