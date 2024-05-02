import random


def values_validation(total):
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
        else:
            if num not in [1, 2, 3]:
                print("Possible values: '1', '2' or '3'")
            elif num > total:
                print("Too many pencils were taken")
            else:
                return num


def num_of_pencils_to_take(pencils_left):
    if pencils_left == 1:
        return 1
    elif pencils_left == 5 or (pencils_left - 5) % 4 == 0:
        return random.randint(1, 3)
    elif pencils_left == 4 or (pencils_left - 4) % 4 == 0:
        return 3
    elif pencils_left == 3 or (pencils_left - 3) % 4 == 0:
        return 2
    elif pencils_left == 2 or (pencils_left - 2) % 4 == 0:
        return 1


print("How many pencils would you like to use:")
while True:
    try:
        num_of_pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if num_of_pencils <= 0:
            print("The number of pencils should be positive")
        else:
            break


print("Who will be the first (John, Jack):")
while True:
    who_first = input()
    if who_first != 'John' and who_first != 'Jack':
        print("Choose between 'John' and 'Jack'")
    else:
        break

while num_of_pencils > 0:
    print('|' * num_of_pencils)
    if who_first == 'John':
        print("John's turn:")
        num = values_validation(num_of_pencils)
        who_first = 'Jack'
    else:
        print("Jack's turn:")
        num = num_of_pencils_to_take(num_of_pencils)
        print(num)
        who_first = 'John'

    num_of_pencils -= num

    if num_of_pencils == 0:
        print(who_first, "won!")