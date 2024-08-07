# código de geração do gráfico 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('gasolina.csv')

fig = sns.lineplot(data=df, x=df['dia'], y=df['venda'])
fig.set(xlabel ="Dia X", ylabel = "Venda", title ='Gasolina')
plt.savefig('gasolina.png')