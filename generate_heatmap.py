import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('archive/pima_diabetes_data.csv')
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap des corrélations du dataset Pima Diabetes')
plt.tight_layout()
plt.savefig('heatmap.png')
print('heatmap.png generated')
