import sys
import numpy as np

lis = [12,20,30,50]
print(sys.getsizeof(lis))

arr = np.array([12,20,30,50])
print(arr.itemsize*arr.size)
