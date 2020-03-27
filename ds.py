import statistics as st
import pandas as pd

df = pd.read_excel("toyota.xlsx")
Mean=st.mean(df['Price'])
print("Mean of Price :",Mean)
Median=st.median(df['Price'])
print("Median of Price :",Median)
Mode = st.mode(df['Price'])
print("Mode of Price :" , Mode)
std=st.stdev(df['Price'])
print("stdev of Price :",std)
vari=st.variance(df['Price'])
print("Variance of Price :",vari)
