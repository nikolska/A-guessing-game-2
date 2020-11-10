import time


def guess():
    print('Choose number between 0 and 1000')
    time.sleep(5)
    min_num = 0
    max_num = 1000
    while True:
        guessing = int((max_num - min_num) / 2) + min_num
        print('I guess your number is:', guessing)
        x = input('Too big, too small or guessed? ').lower()
        if x == 'guessed':
            print('I guess your number!')
            break
        else:
            if x == 'too big':
                max_num = guessing
            else:
                if x == 'too small':
                    min_num = guessing
                else:
                    print('Do not cheat!')


if __name__ == '__main__':
    guess()
