import timeit


TIMES = 10000

SETUP = """
import random
the_list = random.sample(range(10000), 10000)
def do_some_work(c):
    return c % 2
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))


clock('listcomp:    ', '[n for n in the_list if n % 2]')
clock('listcomp + func:    ', '[n for n in the_list if do_some_work(n)]')
clock('filter + lambda:    ', 'list(filter(lambda n: n % 2, the_list))')
clock('filter + func:     ', 'list(filter(do_some_work, the_list))')
