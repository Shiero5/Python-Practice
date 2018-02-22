import numpy
from matplotlib import pyplot
import time
import re

def argToStr(arg):
    if isinstance(arg, list) and len(arg) > 3:
        return "[" + argToStr(arg[0]) + "," + argToStr(arg[1]) + ", ...]"
    else:
        return str(arg)

def evalWithTime(f,arg):
    fn = re.search('^([a-zA-Z0-9_]+) ', str(f)[10:]).group(0)
    s = fn + "(" + argToStr(arg) + ")"
    # print("evaluating ", s, " ... ", end = "")
    # print("evaluating ", s, " ... ")
    start = time.time()
    if isinstance(arg,tuple):
        f(*arg)
    else:
        f(arg)
    et = time.time() - start
    # print("finished in ", et, " seconds.")
    return et

def bench(f,args):
    if isinstance(args[0],tuple):
            x = [i[1] for i in args]
            y = [evalWithTime(f,i[0]) for i in args]
    else:
            x = [i for i in args]
            y = [evalWithTime(f,i) for i in args]
    return (x,y)

def xscaleLog():
    pyplot.xscale("log")

def yscaleLog():
    pyplot.yscale("log")

def xscaleLinear():
    pyplot.xscale("linear")

def yscaleLinear():
    pyplot.yscale("linear")

def plot(d):
    pyplot.plot(d[0],d[1])
    pyplot.show()
