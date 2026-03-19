import numpy as np 

a = np.array([[1, 2], [3, 4]])
#print(a)
#print(a.T)

#print(a.sum())
#print(a.mean())
#print(a.max())

#print(a.sum(axis=0))
#print(a.sum(axis=1))


N1=np.array([2, 4, 6, 8])

# rows = neurons (N1, N2, N3)
# columns = timepoints (t1, t2, t3, t4)

neurons = np.array([
    [2, 4, 6, 8],   # N1
    [1, 3, 5, 7],   # N2
    [9, 2, 4, 1]    # N3
])

#print(neurons.argmax(axis=1))

#SLICING MATRICES

#print(neurons[0])     
#neurons[0] → entire first row → N1's activity across all timepoints

#print(neurons[0, 2]) 
#neurons[0, 2] → single value → N1's activity at t3


#print(neurons[:, 2]) 
#print third column
#print(neurons[1:3, :])
#print second and third rows


print(neurons[1, 0:2])