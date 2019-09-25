import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines import Line2D
import numpy as np
import pandas as pd
from matplotlib import cm
from IPython.display import clear_output

# O site UCI repository forne uma grande variedade de conjunto de dados
# Utilizado: https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data

data = pd.read_csv
	('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', 
	   header = None
)

# Atribuindo os nomes corretos a cada variável
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

# data.head(n) -- Visualiza as n primeiras linhas

# A variavel de interesse é a qualidade do vinho
data = data[data['Quality']!=2] # filtragem das classes
data['Quality'].value_counts() # freq por classe


# Separando os vilhos em relação à qualidade dos mesmos
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

# Visualização das 4 variáveis escolhidas
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
