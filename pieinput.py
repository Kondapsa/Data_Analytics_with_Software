import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fil = input("Enter your Excel filename:  ")
df = pd.read_excel(fil)
var1 = input("Enter Variable:  ")
plt.pie(df[var1])
plt.show()
