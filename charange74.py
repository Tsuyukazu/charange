numbers = [1,3,5,7.9]

while True:
    answer = input('Guess a number or type q to quit. : ')
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print('please type a number or type q to quit.')
    if answer in numbers:
        print('You guessed correctly!')
    else:
        print('You guessed incorrectly!')

