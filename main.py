import time


def guess():
    '''
    Function guess checks the expected user number, replacing the max or min limits
    of the possibility of finding the number.

    :min_num: minimum border, type - int
    :max_num: maximum border, type - int
    :attempts: number of computer attempts, type - int
    :guessing: computer number selection algorithm, type - int
    :user_answer: the user's answer, entered through the keyboard, type - string
    '''
    print('Choose number between 0 and 1000 and i will try to guess it')
    time.sleep(5)
    min_num = 0
    max_num = 1000
    attempts = 0
    while True:
        guessing = int((max_num - min_num) / 2) + min_num
        print('I guess your number is:', guessing)
        user_answer = input('Too big, too small or guessed? ').lower()
        if user_answer == 'guessed':
            print(f'I win! I guessed your number in {attempts} tries!')
            break
        else:
            if user_answer == 'too big':
                max_num = guessing
                attempts += 1
            else:
                if user_answer == 'too small':
                    min_num = guessing
                    attempts += 1
                else:
                    print('Do not cheat!')


if __name__ == '__main__':
    guess()
