
def fibonacci(n):
    # """
    # input <--
    # """
    if n <= 1:
        return (n)
    else:

        return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    if n == 1:
        return 1
    elif n == 0:
        return 2
    else:
        return(lucas(n-1)+lucas(n-2))
