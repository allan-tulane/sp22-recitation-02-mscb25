"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  
  if n <= 1:
    return n
  else:
    return a*simple_work_calc(n//b,a,b)+n

def test_simple_work():
	
	assert work_calc(10, 2, 2) == 36
	assert work_calc(20, 3, 2) == 230
	assert work_calc(30, 4, 2) == 650
 

def work_calc(n, a, b, f):
  if n <= 1:
    return n
  else:
    return a*work_calc(n//b,a,b,f) + f(n)

def span_calc(n, a, b, f):
  
  if n <= 1:
    return n
  else:
    return span_calc(n//b,a,b,f) + f(n)

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
assert work_calc(20, 1, 2,lambda n:n*n) == 530
assert work_calc(30, 3, 2,lambda n: n) == 300

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
    work_fn1 = lambda n: work_calc(n,2,2,lambda n:n*n)
    work_fn2 = lambda n: work_calc(n,2,2,lambda n:1)
    result.append((
			n,
			work_calcwork_fn1(n),
			work_fn2(n)
			))
    return result

def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
  work_fn1 = lambda n: work_calc(n,2,2,lambda n:n*n)
  work_fn2 = lambda n: work_calc(n,2,2,lambda n:1)
  res = compare_work(work_fn1, work_fn2)
  print(res)

