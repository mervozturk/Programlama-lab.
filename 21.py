import random
def shellSort(arr):

    n = len(arr)
    gap = n//2
    karsilastirmasayisi=0
    yerdegeistirmesayisi=0

    while gap > 0:
        for i in range(gap, n):
            karsilastirmasayisi+=1
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                karsilastirmasayisi+=1
                yerdegeistirmesayisi+=1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr,'karsılastırma:',karsilastirmasayisi,'yerdegistirme:',yerdegeistirmesayisi

def get_n_random_integer(n):
    numbers=[]
    for i in range(n):
        s=random.randint(-100,100)
        numbers.append(s)
    return numbers

arr =get_n_random_integer(100)

print ("Array before sorting:",arr)

n=shellSort(arr)

print ("\nArray after sorting:",n)
