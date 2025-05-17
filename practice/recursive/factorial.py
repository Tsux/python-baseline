
def factorial_1st(n, n_minus=1, accum=0):
    accumulate = accum
    if n - n_minus > 0:
        accumulate = accumulate + (n * (n-n_minus))
        #print(f'{n}!{n-n_minus}={n * (n - n_minus)} \t| accum={accumulate}')
        return factorial_1st(n, n_minus+1, accumulate)
    else:
        return accumulate


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

fact_base = 7
print(f"{fact_base}!={factorial(fact_base)}" )