import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1: Create two charts using list and dataframe

plt.plot([1, 2, 3, 4, 5])
plt.plot(pd.DataFrame([9, 5, 3, 7]))

# 2: Create pie chart with equal explode values.
plt.pie(np.arange(1, 4), explode=[0.1, 0.1, 0.1, 0.1])

# 3: Create a scatter chart with circle marker, alpha = 0.4, and size = 50.
x = np.random.randn(200)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.4, s=50)

