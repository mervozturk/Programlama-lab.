import random

def get_n_random_integer(n):
    numbers=[]
    for i in range(n):
        s=random.randint(-100,100)
        numbers.append(s)
    return numbers

def get_mean_for_n_integer(numbers):
    toplam=0
    kactane=0
    for sayi in numbers:
        toplam=toplam+sayi
        kactane+=1

    return toplam/kactane

def get_std_for_n_integer(numbers):
    toplam=0
    kactane=0
    ort=get_mean_for_n_integer(numbers)
    for sayi in numbers:
        toplam=toplam+(sayi-ort)**2
        kactane+=1

    var1=toplam/(kactane-1)
    std_1=var1**0.5

    return std_1
def normalize(numbers):
    new_numbers=[]
    ortalama=get_mean_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)
    for x in numbers:
        new_x=(x-ortalama)/standart_sapma
        new_numbers.append(new_x)

    return new_numbers
def get_mean_one_std_neighbor_ration(numbers):
    kactane=0
    toplamsayı=0
    ortalama=get_mean_for_n_integer(numbers)
    std=get_std_for_n_integer(numbers)
    low=ortalama-std
    high=ortalama+std

    for x in numbers:
        toplamsayı+=1
        if(x>low and x<high):
            kactane+=1

    return kactane/toplamsayı

sayılar=get_n_random_integer(10)
ortalama=get_mean_for_n_integer(sayılar)
std=get_std_for_n_integer(sayılar)
n=normalize(sayılar)
yakın=get_mean_one_std_neighbor_ration(sayılar)
print (sayılar)
print ("ort:",ortalama)
print ("std:",std)
print ("normalize:",n)
print ("yakın eleman yüzdesi:",yakın)



sayılar2=[75,32,25,14,47]
lenght=len(sayılar2)
print ("one:",sayılar2)

for i in range(1,lenght):
    for j in range(i,0,-1):
        if(sayılar2[j]<sayılar2[j-1]):
            t=sayılar2[j-1]
            sayılar2[j-1]=sayılar2[j]
            sayılar2[j]=t

print ("two:",sayılar2)

