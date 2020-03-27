import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fil = input("Enter your Excel filename:  ")
df = pd.read_excel(fil)
var1 = input("Enter First variable:")
var2 = input("Enter Second variable:")
df1 = df[var1]
df2 = df[var2]
plt.bar(df1,df2,label = 'cars',color = 'c')
plt.xlabel(var1)
plt.ylabel(var2)
plt.title("Bar Graph of cars")
plt.legend()
plt.show()
