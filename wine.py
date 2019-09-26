import matplotlib.pyplot as plt
import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines import Line2D
import numpy as np
import pandas as pd
from matplotlib import cm
from IPython.display import clear_output

# The website UCI repository provide a wide range of data sets
# Used: https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data

data = pd.read_csv
	('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', 
	   header = None
)

# Assigning the correct names to each variable
data.clumns = [
	'Quality', 
	'Alcohol',
	'Malic acid',
	'Ash',
	'Alcalinity of ash',
	'Magnesium',
	'Total phenols',
	'Flavanoids',
	'Nonflavanoid phenols',
	'Proanthocyanins',
	'Hue',
	'OD280/0D315 of diluted wines',
	'Proline',
]

# data.head(n) -- Display the first n lines

# The variable of interest is the quality of the wine.
data = data[data['Quality']!=2] # filtragem das classes
data['Quality'].value_counts() # freq por classe


# Separating wines by quality
sns.pairplot(
	data,
	hue='QUality',
	vars=[
		d for d in data.columns if d!='Quality'
	]
)

# Filtrando 4 variaveis
data = data[[
	'Quality',
	'OD280/OD315 of diluted wines',
	'Hue',
	'Proline'
]]

# Visualization of the 4 chosen variables
fig = plt.figure()

ax = fig.gca(projection='3d')

colors = data['quality'].map({1:'g', 3:'r'}).values

ax.scatter(
	data['OD280/OD315 of diluted wines'],
	data['Hue'],
	data['Proline'],
	c = colors
)

plt.tight_layout()
plt.show()

# straightening the graph
plt.title("Wine Quality")
plt.xlabel('OD280/OD315 of diluted wines')
plt.ylabel('Hue')
ax.set_zlabel('Proline')

Legend_elements = [
	Line2D([0], [0],
		marker='o',
		color='w',
		label='Good',
		markerfacecolor='g',
		markersize=10),
	Line2D([0], [0],
		marker='o',
		color='w',
		label='Bad',
		markerfacecolor='r',
		markersize=10)
]

ax.legend(handles=legend_elements, loc='best')

# Animating the chart
for angle in range(30, 330, 2):
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(
		data['OD280/OD315 of diluted wines'],
		data['Hue'],
		data['Proline'],
		color = colors)
	
	ax.view_init(30, angle)
	
	plt.tight_layout()
	plt.gca()
	clear_output(wait=True)
	plt.show()


	
