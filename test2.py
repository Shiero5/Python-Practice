import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([[1,2,3], [2,3,4],[5,3,3]], index=['a','b','c'], columns=['A','B','C'])
fig, ax = plt.subplots()
ax.pcolor(df)
ax.show()
