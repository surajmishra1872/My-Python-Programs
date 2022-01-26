#import numpy as np
#print(np.__version__)
#import numpy as np
#arr = np.array([[1, 2, 3], [4, 5, 6]])
#print(arr)
##import numpy as np
##
##a = np.array(42)
##b = np.array([1, 2, 3, 4, 5])
##c = np.array([[1, 2, 3], [4, 5, 6]])
##d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
##
##print(a.ndim)
##print(b.ndim)
##print(c.ndim)
##print(d.ndim)

import numpy as np
##arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12],ndmin=5)
##arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
##arr2=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
##arr3=np.array(12)
##print(arr3)
#print(arr)
##print(arr1)
##print(arr2)
##print(arr.ndim)
##print(arr1.ndim)
##print(arr2.ndim)
##print(arr3.ndim)
#print(arr2[1,0,4])
#newarr = arr.reshape(2,3,2)
#print(newarr)


arr = np.array(arrange(1,12))

newarr = arr.flatten("F")

print(newarr)

