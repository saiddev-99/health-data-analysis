import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement des données
# Remplace par le chemin de ton fichier téléchargé
df = pd.read_csv('archive/pima_diabetes_data.csv')

# Nettoyage des données

df['BMI'] = df['BMI'].replace(0, np.nan)

      ## Visualisation de la corrélation entre les variables
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Corrélation entre les indicateurs de santé")

# Visualisation de la distribution du taux de glucose en fonction du diagnostic
plt.figure(figsize=(8, 6))
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title("Distribution du taux de Glucose selon le diagnostic")
plt.xticks([0, 1], ['Sain (0)', 'Diabétique (1)'])

#Compare la distribution de l'insuline ou du glucose chez les patients sains vs les patients malades.
plt.figure(figsize=(8, 6))
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title("Distribution du taux de Glucose selon le diagnostic")
plt.xticks([0, 1], ['Sain (0)', 'Diabétique (1)'])
plt.show()

# 2. Premier coup d'œil
print("--- Aperçu des 5 premières lignes ---")
print(df.head())

print("\n--- Informations générales (Types et valeurs manquantes) ---")
print(df.info())

print("\n--- Statistiques descriptives ---")
print(df.describe())