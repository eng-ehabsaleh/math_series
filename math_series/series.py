
def fibonacci(n):
    """
     creating a function that take one parameter
         and then it will calculate the value of that index based on  Fibonacci Series
         and then return this value
    """
    if n <= 1:
        return (n)
    else:

        return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """create a function that take one parameter
        and then calculate the value of that number based on Lucas Numbers series
        and then return the value of that number which be considered as an index to the series"""
    if n == 1:
        return 1
    elif n == 0:
        return 2
    else:
        return(lucas(n-1)+lucas(n-2))


def sum_series(na, n2=0, n3=1):
    if n2 == 0 and n3 == 1 and na <= 1:
        return 1
    elif na > 1 and n2 == 0 and n3 == 1:
        return (sum_series(na-2) + sum_series(na-1))
    elif n2 == 2 and n3 == 1:
        return(sum_series(na-1) + sum_series(na-2))
    else:
        return (sum_series(na-1) + sum_series(na-2))
