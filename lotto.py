from random import randint

def lottery_generator():
    numbers = []
    for number in range(0,6):
        numbers.append(randint(1,50))
    return numbers
    
print("This weeks wining numbers are %s"% lottery_generator())
    