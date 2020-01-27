import timeit


TIMES = 10000

SETUP = """
import random
the_list = random.sample(range(10000), 10000)
def do_some_work(c):
    return c % 2
"""

SETUP2 = """
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
empty_l = []
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))


def clock2(label,  cmd):
    res = timeit.repeat(cmd, setup=SETUP2, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))


clock('listcomp:    ', '[n for n in the_list if n % 2]')
clock('listcomp + func:    ', '[n for n in the_list if do_some_work(n)]')
clock('filter + lambda:    ', 'list(filter(lambda n: n % 2, the_list))')
clock('filter + func:     ', 'list(filter(do_some_work, the_list))')
clock('len(the_list):    ', 'len(the_list)')
clock('the_list.__len__()     ', 'the_list.__len__() ')

print('#'*3, '\n')
clock2('[(color,size) for color in colors for size in sizes] --> ',
       '[ (color, size) for color in colors for size in sizes ]')
clock2('for color in colors: for size in sizes: print((color, size)) --> ',
       '''for color in colors:
              for size in sizes:
                  empty_l.append((color, size))''')

clock2('[(color, size) for size in sizes for color in colors] --> ',
       '[(color, size) for size in sizes for color in colors]')
