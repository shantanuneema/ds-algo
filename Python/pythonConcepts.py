"""
Notes:

In python 3, iteritems(), xrange(), and izip() were replaced by items(), range(), and zip() and all 3 work as iterator (faster)
In python 3, for sorting a list based on conditions requires to use functions (i.e. in SQL), or call functools.cmp_to_key(<function>)

Pure function: a function that returns the same value everytime one call it (use @cache)
"""

import functools
colors = ["red", "blue", "green", "yellow"]

def compare_len(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print(sorted(colors))
print(sorted(colors, key = functools.cmp_to_key(compare_len)))
print(sorted(colors, key = len))

f = open('logfile.txt', 'r')

blocks = []
while True:
    block = f.read(32)
    if block == "": break
    blocks.append(block)
    
blocks = []
for block in iter(functools.partial(f.read, 32), ""):
    blocks.append(block)

# multiple exit points in a loop
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

seq = [1,2,3,4,5,6,7,8,9,10]; target = 5
print(find(seq, target))

def find3(seq, target):
    for i, value in enumerate(seq):
        if value == target: break
    else: return -1
    return i

print(find3(seq, target))

colors = ["red", "blue", "green", "red", "green", "green"]

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1 # cannot use "+=" here (short circuit)
    
print(d)

names = ["raymond", "rachel", "matthew", "roger",
         "melissa", "betty", "judith", "charlie"]
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

    print(d)
    
# dictionary with None values with a given list of keys
print(dict.fromkeys([1,2,3]))

# use of popitems() (atomic)
while d:
    key, value = d.popitem()
    print(key, value)

# Linking dictionaries
import argparse
import os
from collections import ChainMap  

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
       
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
    
# Defining the chainmap  
c = ChainMap(d1, d2, d3) 
print(c)

 # Cache logic (for repeated URLs)
import urllib
def web_lookup(url, saved = {}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# Use cache instead (in front of any pure function)
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

from decimal import *
# factor out temporary context (use of context manager)
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)

# use localcontext
with localcontext(Context(prec = 20)):
    print(Decimal(355) / Decimal(113))

# use of lock
import threading
lock = threading.Lock()

lock.acquire()
try:
    print("Section 1")
finally:
    lock.release()
    
# use this instead (does same as above)
with lock:
    print("Section 1")

import contextlib
# ways to ignore try, except
try:
    os.remove("somefile.csv")
except OSError:
    pass

# use below:
with contextlib.suppress(OSError):
    os.remove("somefile.csv")