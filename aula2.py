import pandas as pd 
import plotly.express as px

#df = pd.read_csv('telecom_users.csv')

#print(df.keys())
#exit()
# df = pd.read_csv('telecom_users.csv', sheet_name="telecom_users") # nome da planilha ou número
df = pd.read_csv('telecom_users.csv',index_col=[0]).reset_index(drop=True) # exclui a coluna de índice


#print(df) # preview da tabela

#exit()

df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors='coerce')

df = df.dropna(how='all', axis=1) # apaga todas as colunas com TODOS (all) os valores vazios

df = df.dropna(how='any', axis=0) # apaga todas as linhas com PELO MENOS (any) um valor vazio

print(df["Churn"].value_counts()) # conta igual group by do mysql
print(df["Churn"].value_counts(normalize=True)) # apresenta em percentual decimal
print(df["Churn"].value_counts(normalize=True).map("{:.2%}".format)) # map é um foreach, neste caso, formata cada valor

# comparar a correlação entre as colunas e a coluna chave da análise

graph = px.histogram(df, x="Aposentado", color="Churn", text_auto=True)

#graph.write_html('aposentado.html', auto_open=True) # gera o resultado em html e abre no navegador

# comparar todas as colunas com outra
for col in df.columns:
	graph = px.histogram(df, x=col, color="Churn", text_auto=True)
	graph.write_html(('gráficos/'+col+'.html'), auto_open=False) # gera o resultado em html e abre no navegador

#graph.show() # só funciona no jupyter

#print(df.info()) # informações da tabela

