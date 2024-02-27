# -*- coding: utf-8 -*-
"""Base de Dados- Unifor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLOZwABaRdFJMDReqLdsnb7tFg_8uQ8S

# Import das bibliotecas
"""

import pandas as pd

"""# Codigo de Tratamento de Dados"""

#Import do Arquivo da base de dados de Dengue
path_dengue = 'Base de Dengue3.csv'

#Import do Arquivo da base de dados de Alunos
path_alunos = 'Base de Alunos3.csv'

#Lendo o arquivo "path_dengue"
df_dengue = pd.read_csv(path_dengue, sep=';')

#Lendo o arquivo "path_alunos"
df_alunos = pd.read_csv(path_alunos, sep=';')

#'len' = tamanho de linhas do dataframe alunos
len(df_alunos)

#'len' tamanho de linhas do dataframe dengue
len(df_dengue)

df_alunos

df_dengue

#listagem da coluna 'Nomes' do datafame de dengue
lista_nomes_alunos = list(df_alunos['Nome'])

#criando um dataframe de alunos com dengue, chamando apenas os nomes dos alunos que tiveram dengue
df_alunos_com_dengue = df_dengue[df_dengue['Nome'].isin(lista_nomes_dengue)]

df_alunos_com_dengue

#Informação do dataframe de alunos com dengue = como os dados são e quantas linhas nao nulas eles tem
df_alunos_com_dengue.info()

#Export do novo dataframe tratado (alunos com dengue)
df_alunos_com_dengue.to_excel('Alunos com Dengue3.xlsx')