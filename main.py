import numpy as np
import matplotlib.pyplot as plt

data = {'c':20,'c++':15,'Java':30,'Python':35}

course = list(data.keys())
values = list(data.values())

print(course)
print(values)

plt.bar(course, values, color = 'maroon', width = 0.4)
plt.xlabel("Courses Offered")
plt.xlabel("Students Enrolled")
plt.title("Students Enrolled In Codingal Courses")
plt.show()