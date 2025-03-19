import numpy as np 

a = np.arange(6).reshape(2,3) + 10
print("The numpy array is \n")
print(a)
print("\n")

print("****** np.argmax Usage ******\n")
print("The index of maximum value from the flattened version is \n")
print(np.argmax(a))
print("\n")

print("The indices of maximum values along the column are \n")
print(np.argmax(a, axis=0))
print("\n")

print("The indices of maximum values along the row are \n")
print(np.argmax(a, axis=1))
print("\n")



print("****** np.argmin Usage ******\n")

print("The index of minimum value from the flattened version is \n")
print(np.argmin(a))
print("\n")

print("The indices of minimum values along the column are \n")
print(np.argmin(a, axis=0))
print("\n")

print("The indices of minimum values along the row are \n")
print(np.argmin(a, axis=1))
print("\n")


print("****** np.sort Usage ******\n")

b = np.array([[1,4],[3,1]])
print("Numpy array before applying the sorting operation \n")
print(b)
print("\n")
print("The result of sorting along the last axis \n")
print(np.sort(b))
print("\n")

print("The result of sorting the flattened version of the array \n")
print(np.sort(b, axis=None))
print("\n")

print("The result of sorting along the first axis \n")
print(np.sort(b, axis=0))
print("\n")

