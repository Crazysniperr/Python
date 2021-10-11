from random import choices
class lottery:
    def __init__(self):
        self.lst = ('1','2','3','4','5')
        self.lst1=[]
        self.myticket = ['4','5','1','2']

    def roll_lottery(self):
        for i in range(4):
            roll = choices(self.lst)
            for item in roll:
                self.lst1.append(item)
        print(f'Any ticket matching these four numbers or letters {self.lst1} wins a prize')

    def my_ticket(self,count = 0):
        while self.lst1 != self.myticket:
            count += 1
        print(f'The number of time loop runned is {count}')

my_lottery = lottery()
my_lottery.roll_lottery()
my_lottery.my_ticket()
