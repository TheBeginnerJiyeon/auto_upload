number=[]

for i in range(11):
    number.append(i)

print(number)

num=[i for i in range(11)]
print(num)

# list_comprehension

list_x=[x for x in range(11)]
print(list_x)

odds=[x for x in range(11) if x%2==1]
print(odds)

odd2=[x for x in range(11) if x%2==1 and x<5]
print(odd2)

odd3=[]
for x in range(10+1):
    if x%2==1 and x<5:
        odd3.append(x)

odd4=[x for x in range(11) if x%2==1 if x<7]
print(odd4)

# 이중 for, list comprehension
가게=['올리브영','세븐일레븐','엘지25']
제품=['폰 충전기','물티슈','콜라']

살거=[(x,y) for x in 가게 for y in 제품]
print(살거)

