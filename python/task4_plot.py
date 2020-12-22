import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 


df = pd.read_excel('task4.xlsx', engine='openpyxl')

fig, ax = plt.subplots()
ax.plot(df["out"])

fig, ax = plt.subplots()
ax.plot(df["out_mean"])