import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datasets used are seaborn built-in datasets

tips = pd.read_csv('tips.csv')

print(tips.head())

sns.set_theme()
# sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='smoker', size='size')
# plt.show()

print()

# Iris dataset
iris = sns.load_dataset('iris')
print(iris.head())

sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data='iris')
plt.show()
