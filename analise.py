import pandas as pd
import numpy as np

#lendo o data frame

df_obesidade = pd.read_csv("obesity_cleaned.csv", index_col=0)

#limpando os dados do dtaframe, criando uma coluna de nome 'obesity' que contera os valores de obesidade. Transfrome para float as colunas quer por ventura importadas como strings

df_obesidade['Obesity (%)'].value_counts() #vendo os dados que tenho na coluna obesidade

df_obesidade.columns #visualizando as colunas que possue meu dataframe

df_obesidade['Obesity'] = df_obesidade['Obesity (%)'].apply(lambda x: x.split()[0])
df_obesidade.loc[df_obesidade['Obesity'] == 'No', 'Obesity'] = np.nan


df_obesidade['Obesity'] = df_obesidade['Obesity'].dropna()

df_obesidade['Obesity'] = df_obesidade['Obesity'].apply(lambda x: float(x)) #transformado os dados para float
df_obesidade['Year'] = df_obesidade['Year'].apply(lambda x: int(x)) #transformando os dados para inteiro

df_obesidade

df_obesidade.set_index('Year', inplace=True)


#qual o percentual medio de obesidade por sexo no mundo no ano de 2015

df_obesidade[df_obesidade.index == 2015].groupby('Sex').mean()
