import numpy as np
array = [1,2,3,4,5,6]
nparray = np.array(array)
tolerance = 3
mean = np.mean(nparray)
standarddev = np.std(nparray)
print("Mean = ",mean, "standard deviation = ",standarddev)
print('\n')

print("range for", tolerance, "deviations = ", mean - standarddev * tolerance, "-", mean + standarddev * tolerance)
