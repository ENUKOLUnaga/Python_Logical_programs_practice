import numpy as np

print(np.eye(3))
print(np.linspace(0,1,5))
print(np.arange(0,10,2))

"""arr=np.arange(6)
print(arr)
print(arr.reshape(2,3))
"""

"""arr=np.array([[1,2,3],
              [4,5,6]])

flat=arr.flatten()
flat[0]=200
print(flat)
print(arr)

rave=arr.ravel()
rave[0]=100
print(rave)
print(arr)
"""

"""print(np.random.rand())
"""
"""np.random.seed(42)
print(np.random.choice([10,20,30,40],size=3))
"""

arr=np.array([1,2,3,4])
"""np.random.shuffle(arr)
print(arr)
"""
"""mask=arr>2
print(arr[mask])

arr[arr<2]=3
print(arr)
print(np.split(arr,4))
"""
"""print(np.repeat(arr,2))
print(np.tile(arr,2))
"""

print(np.hsplit(arr,4))
