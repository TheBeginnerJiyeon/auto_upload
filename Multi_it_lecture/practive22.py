# lambda 연습
# use map(), filter(), and reduce() 
from functools import reduce


numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

mapped=map(lambda x: x**2,numbers)
print(type(mapped))
print(list(mapped))

filterd=filter(lambda x:x%2==0, numbers)
print(type(filterd))
print(list(filterd))

reduced= reduce(lambda x,y: x*y,numbers)
print(reduced)




