def my_vectors_ınner_product(v,w):
    size=(len(v))
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]


    t=0
    for i in range(size):
        t=t+my_result[i]

    return t

def my_vector_scalar_product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]

    return my_result

def my_vector_substraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]-w[i]

    return my_result

def my_vector_addition(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]+w[i]

    return my_result

a=[1,2,3,2,4,6]
b=[3,4,7,5,9,5]

print("a vektörü:",a)
print("b vektörü:",b)
print ("-------------------------")
print("a ve b vektörünün toplamı:",my_vector_addition(a,b))
print("a-b vektörü:",my_vector_substraction(a,b))
print("a vektörünün 5 ile çarpımı:",my_vector_scalar_product(5,a))
print("b vektörünün 5 ile çarpımı:",my_vector_scalar_product(5,b))
print("a*b vektörünün elemanları toplamı:",my_vectors_ınner_product(a,b))



