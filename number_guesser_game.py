import random
random_number = random.randint(1,10)
# print(random_number)
confirmation = input('Do you want to play (yes/no): ')
print('Guess the number between 1 to 10')
count = 0
while count!=3:

    if confirmation != 'yes':
        break
    else :

        user_number = int(input('Enter the number: '))

        if user_number > random_number:
            if user_number > (random_number+1):
                print('you are far high from the number ')
            else:
                print('warmer but high')
        elif user_number < random_number:
            if user_number < (random_number-1):
                print('you are far low from the number ')
            else:
                print('warmer but low')
        elif user_number == random_number:
            print('CONGRATULATIONS! You guessed the right number')
            break
        count += 1
        print(f'You have {3-count} chances left')
if count == 3:
    print('SORRY! You have exceeded your chances')
