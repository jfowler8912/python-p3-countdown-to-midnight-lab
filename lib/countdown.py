import time
def countdown(number = 10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print( "HAPPY NEW YEAR!")


def countdown_with_sleep(number):
    time.sleep(1)
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print( "HAPPY NEW YEAR!")
