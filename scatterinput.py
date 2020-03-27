import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fil = input("Enter your Excel filename:  ")
df = pd.read_excel(fil)
fig, ax = plt.subplots()
var1 = input("Enter First Variable:  ")
var2 = input("Enter Second variable:  ")
my_scatter_plot = ax.scatter(
    df[var1],
    df[var2],
    cmap = plt.cm.Reds,
    vmin = 0,
    edgecolor = "#6b0c08",
    linewidth = 0.75
    )
ax.set_xlabel(var1)
ax.set_ylabel(var2)
ax.set_title("Scatter plot of cars")
plt.show()
