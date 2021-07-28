
import numpy as np

m_array = np.array(list(map(int,"1 2 3 4 5 6 7 8 9".split())))

r_array = np.reshape(m_array,(3,3))

print(r_array)