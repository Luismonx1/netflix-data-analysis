#%%
import pandas as pd
import matplotlib.pyplot as plt

nomes_portugues = {
    'show_id': 'id_do_show',
    'type': 'tipo',
    'title': 'titulo',
    'director': 'diretor',
    'cast': 'elenco',
    'country': 'pais',
    'date_added': 'data_de_adicao',
    'release_year': 'ano_de_lancamento',
    'rating': 'classificacao',
    'duration': 'duracao',
    'listed_in': 'listado_em',
    'description': 'descricao',
}

netflix = pd.read_csv('../data/netflix_titles.csv')
netflix.fillna('Desconhecido', inplace=True)
netflix = netflix.rename(columns = nomes_portugues)

#%%

#Quantidade de Shows por País em um determinado ano de lançamento

netflix['pais'] = netflix['pais'].str.split(',')
netflix = netflix.explode('pais')
netflix['pais'] = netflix['pais'].str.strip()

netflix_ano = netflix[(netflix['ano_de_lancamento'] >= 2000) & (netflix['ano_de_lancamento'] <= 2020)]
df_ano_pais = netflix_ano.groupby(['ano_de_lancamento', 'pais']).size().reset_index( name = 'quantidade')

df_paises = df_ano_pais.groupby('pais')['quantidade'].sum().reset_index(name='quantidade')
df_paises = df_paises[df_paises['pais'] != 'Desconhecido']

top_10_paises = df_paises.sort_values(by='quantidade', ascending=False).head(10)
top_10_paises.head(10)

plt.barh(top_10_paises['pais'], top_10_paises['quantidade'])
plt.title('Top 10 Países com Mais Shows na Netflix (2000-2020)')
plt.xlabel('Quantidade de Shows')
plt.ylabel('País')

ax = plt.gca()
ax.spines[['right','left','top','bottom']].set_visible(False)
ax.grid(axis='x', color='black', alpha=0.5)
ax.tick_params(axis='both', length=0)


# %%
