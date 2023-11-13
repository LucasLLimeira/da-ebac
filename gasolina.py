import seaborn as sns
import pandas as pd
import csv

gasolina_df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette ='pastel')
  grafico.set(title='Preço da gasolina por dia na cidade de São Paulo', xlabel='Dias', ylabel='Preço (R$)');

grafico.get_figure().savefig('gasolina.png')