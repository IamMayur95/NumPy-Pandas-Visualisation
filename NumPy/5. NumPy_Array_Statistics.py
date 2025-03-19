import numpy as np 

a = np.arange(6).reshape(2,3) + 10
print("The numpy array is \n")
print(a)
print("\n")

print("****** np.mean Usage ******\n")
print("The mean of the flattened version of array is \n")
print(np.mean(a))
print("\n")

print("The mean of each individual column is  \n")
print(np.mean(a, axis=0))
print("\n")

print("The mean of each individual row is \n")
print(np.mean(a, axis=1))
print("\n")



print("****** np.std Usage ******\n")

print("The standard deviation of the flattened version of array is \n")
print(np.std(a))
print("\n")

print("The standard deviation of each individual column is  \n")
print(np.std(a, axis=0))
print("\n")

print("The standard deviation of each individual row is \n")
print(np.std(a, axis=1))
print("\n")



print("****** np.var Usage ******\n")

print("The variance of the flattened version of array is \n")
print(np.var(a))
print("\n")

print("The variance of each individual column is  \n")
print(np.var(a, axis=0))
print("\n")

print("The variance of each individual row is \n")
print(np.var(a, axis=1))
print("\n")


