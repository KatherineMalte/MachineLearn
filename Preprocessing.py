import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Generar datos de ejemplo
np.random.seed(10)
data = {
    'Grupo A': np.random.normal(loc=0, scale=1, size=100),
    'Grupo B': np.random.normal(loc=1, scale=1.5, size=100),
    'Grupo C': np.random.normal(loc=2, scale=0.5, size=100)
}

# Crear un DataFrame
#df = pd.DataFrame(data)

# Crear el boxplot
#plt.figure(figsize=(10, 6))
#sns.boxplot(data=df)
#plt.title('Boxplot de Grupos A, B y C')
#plt.xlabel('Grupos')
#plt.ylabel('Valores')
#plt.grid(True)

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot
filename="automobileEDA.csv"
df.head()

df = pd.read_csv(filename, header=0)
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()