
def sndmax(array):
    v = array[0]
    for i in range(0,len(array)):
        if v < array[i]:
            v = array[i]
    #この時点でvは最大値となる
    v2 = v - array[0]
    s = 0
    for i in range(0,len(array)):
        if (v - array[i] == 0) and (s == 0):
            s = s - 1
        elif (v - array[i] == 0) and not(s == 0):
            return array[i]
        elif (v2 > v - array[i]):
            v2 = v - array[i]



    v3 = v - v2
    return v3






array2 = [876,12,431,65,67,12,526,34,7,454,591,432,876,998]
array3 = [-23,-32,0,0,-1,-2,-2,-67,-9,-44]

print(sndmax(array2))
print(sndmax(array3))
