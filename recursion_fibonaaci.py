def fibonnaci(number):
    '''Fibonacci Series'''
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonnaci(number-1) + fibonnaci(number-2)

print(fibonnaci(8))
