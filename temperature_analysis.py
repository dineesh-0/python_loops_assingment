#------------------TASK 1------------------
print("TASK 1")
import numpy as np
temps_celisius=np.array([22,25,28,24,26])
temps_fah=(temps_celisius*1.8)+32
print(f"Celsius : {temps_celisius}\nFahrenheit : {temps_fah}")
print(f"avregae fahrenheit : {temps_fah.mean()}")
print("\n\n\n")

#--------------------TASK 2------------
print("TASK 2")

import numpy as np
scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(f"Shape : {scores.shape}")
print(f"Total Elements : {scores.size}")
print(f"High Score : {scores.max()}")
print(f"Lowest Score : {scores.min()}")
print(f"Range : {scores.max()-scores.min()}")

print("\n\n\n")
#-------------------TASK 3----------------------------

print("TASK 3")
import numpy as np
import time
num_arr=np.arange(1,50001)
num_list=list(range(1,50001))

start_np = time.perf_counter()
res_np = np.sum(num_arr)
end_np = time.perf_counter()
time_np = end_np - start_np

start_l = time.perf_counter()
res_l = sum(num_list)
end_l = time.perf_counter()
time_l = end_l - start_l

speed=time_l/time_np
print(f"NmuPy sum: {res_np}")
print(f"Python sum :{res_l}")
print(f"NumPy time : {round(time_np,4)}")
print(f"Python time : {round(time_l,4)}")
print(f"NumPy is {round(speed,4)}x faster ")