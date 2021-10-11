import random
r_p_s = ['rock','paper','scissor']
user_lst = []
count = 0
def game(user_input):
    if 'paper' in guess:
        if user_input == 'rock':
            print('Computer has won')
        elif user_input == 'paper':
            print('Computer and Player has tied')
        elif user_input == 'scissor':
            print('Player has won')
    elif 'rock' in guess:
        if user_input == 'scissor':
            print('Computer has won')
        elif user_input == 'rock':
            print('Computer and Player has tied')
        elif user_input == 'paper':
            print('Player has won')

    elif 'scissor' in guess:
        if user_input == 'paper':
            print('Computer has won')
        elif user_input == 'scissor':
            print('Computer and Player has tied')
        elif user_input == 'rock':
            print('Player has won')
while True:
    confirmation = input('Do you want to play (yes/no): ')
    if confirmation == 'yes':
        user_count = int(input('How many tries do you want to play: '))
        while count!=user_count:
                # print(user_lst)
                guess = random.choices(r_p_s)
                # print(guess)
                user_input = (input('Enter your choice: '))
                user_lst.append(user_input)
                # for j in user_lst:
                #     print(j)
                game(user_input)
                for i in guess:
                    print(f'Computer chose {i}')
                count +=1
                user_lst.clear()

    elif confirmation == 'no':
        break
    else:
        print('Enter the right option')
        break
