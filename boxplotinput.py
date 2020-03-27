import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fil = input("Enter your Excel filename:  ")
df = pd.read_excel(fil)
fig, ax = plt.subplots()
var1 = input("Enter variable:")
my_scatter_plot = ax.boxplot(
    df[var1],
    )
ax.set_title("Box plot of cars")
plt.show()
