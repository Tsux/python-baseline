# Fibonacci Sequence
# 0, 1 ...
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
def fibo(n: int, series=None, cycle=1):
    series = [0, 1] if series is None else series
    current = series[len(series) - 1]
    prev = series[len(series) - 2]
    if cycle==n or n<=0:
        return series
    #print(f'{current + prev}', end=' ')
    series.append(current + prev)
    fibo(n, series=series, cycle=cycle+1)

def fibo2(stop_number, current=1, prev=0, cycle=1):
    if stop_number >= (current + prev):
        return
    if cycle == 1:
        print(f'\nFibonacci Series up to {stop_number}: \n{prev} {current}', end=' ')
    print(f'{current + prev}', end=' ')
    fibo2(stop_number, current=current + prev, prev=current, cycle=cycle+1)

# Python program to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n, [0, n]
   else:
       item_c, series = recur_fibo(n - 1)
       item = item_c + recur_fibo(n - 2)[0]
       series.append(item)
       return item, series
#fibo(25)
last, fibo_series = recur_fibo(10)
print(' '.join(map(str, fibo_series)))
