
from functools import reduce
def test(a):
    if a>=3:
        return a

data=filter(test,[1,2,3,4,5,6,8])
print(list(data))


data=filter(lambda a:(a>=3),[1,2,3,4,5,6,7])
print(list(data))

data=reduce(lambda a,b:a+b,[1,2,3,4])
print(data)

data=map(lambda a:a+a , filter(lambda a:(a>3),[3,4,5,6]))
print(list(data))

data=filter(lambda a:(a>9) , map(lambda a:a*a,[3,4,5,6]))
print(list(data))

a=[1,2,3,4,5,6]
a.remove(1)
a.remove(2)
a.remove(3)

print(a)
print(a)

integer_list = []
n = int(input())
for i in range(n):
    integer_list.append(input())
listt = map(int, integer_list)

tuplee = tuple(listt)
print(hash(tuplee))


