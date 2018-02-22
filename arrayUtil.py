import copy

def make1d(n,value=0):
    return [copy.deepcopy(value) for i in range(0,n)]

def make2d(n,m,value=0):
    return [make1d(m,value) for i in range(0,n)]

def make3d(n,m,k, value=0):
    return [make2d(m,k,value) for i in range(0,n)]


