import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fil = input("Enter your Excel filename:  ")
df = pd.read_excel(fil)
var1 = input("Enter Variable:  ")
plt.hist(df[var1],bins=20)
plt.xlabel(var1)
plt.ylabel("Number of Cars")
plt.title("Histogram of cars")
plt.show()
