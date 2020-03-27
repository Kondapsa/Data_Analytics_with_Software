import statistics as st
import pandas as pd
from scipy import stats


#Descrptive Statistics
data = pd.read_excel("toyota.xlsx")
Mean=st.mean(data['Price'])
print("Mean of Price :",Mean)
Median=st.median(data['Price'])
print("Median of Price :",Median)
Mode = st.mode(data['Price'])
print("Mode of Price :" , Mode)
std=st.stdev(data['Price'])
print("stdev of Price :",std)
vari=st.variance(data['Price'])
print("Variance of Price :",vari)

print(data.describe())


