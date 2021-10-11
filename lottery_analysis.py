from random import choices
count = 0
lst = ('1','2','3','4','5','6','7','8','9','10','a','b','c','d','e')
lst1=[]
myticket = ['1','2','a','b']
def roll_lottery():
    for i in range(4):
        roll = choices(lst)
        for item in roll:
            lst1.append(item)
    print(f'\n the lottery no. is {lst1}')


 
while True:
    roll_lottery()
    if lst1 != myticket:
        lst1.clear()
        count += 1
        print(f'The number of time loop runned is {count}')
    elif lst1 == myticket:
        print(f'you have won the lottery after {count} times')
        break
