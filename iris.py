import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl 

iris = sns.load_dataset('iris')

# guardar el archivo en un formato csv
iris.to_excel('iris_dataset.xlsx', index=False)

print('Dataset guardado como "iris_dataset.xlsx"')
