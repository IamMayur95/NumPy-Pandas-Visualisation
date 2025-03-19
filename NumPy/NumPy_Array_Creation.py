import numpy as np 

print("****** np.empty Usage ******\n")
a = np.empty(shape=[2,2], dtype=int)
print(a)
print("\n")


print("****** np.eye Usage ******\n")

# N is the number of rows
# M is the number of columns

b = np.eye(N=2, M=2, k=0, dtype=int)
print("For k=0\n")
print(b)
print("\n")

c = np.eye(N=2, M=2, k=1)
print("For k=1\n")
print(c)
print("\n")


print("****** np.identity Usage ******\n")

# n is the dimension of square numpy array

d = np.identity(n=2, dtype=np.float)

print(d)
print("\n")


print("****** np.linspace Usage ******\n")

e = np.linspace(start=1.0, stop=5.0, num=5)
print("Including the stop element\n")
print(e)
print("\n")

f = np.linspace(start=1.0, stop=5.0, num=5, endpoint=False)
print("Excluding the stop element\n")
print(f)
print("\n")

print("****** np.ones Usage ******\n")
g = np.ones(shape=(5,), dtype=int)
print(g)
print("\n")

print("****** np.zeros Usage ******\n")

h = np.zeros(shape=(5,5), dtype=int)
print(h)
print("\n")


