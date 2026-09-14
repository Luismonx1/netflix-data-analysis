# 🎬 Análise Netflix

Análise exploratória do catálogo de filmes e séries da Netflix, usando Python, pandas e Matplotlib, com foco em distribuição por país e produção ao longo do tempo.

---

## ❓ Perguntas de investigação

1. **Quantidade de shows por país**, considerando um determinado intervalo de ano de lançamento.
2. **Títulos mais recentes e mais antigos adicionados por país** ao catálogo.
3. **Diretores com mais filmes**, desconsiderando títulos sem diretor listado.

---

## 📊 Fonte dos dados

Dataset público **"Netflix Movies and TV Shows"**, disponível no Kaggle:
https://www.kaggle.com/datasets/shivamb/netflix-shows

Contém informações sobre filmes e séries do catálogo da Netflix, como título, diretor, elenco, país, data de adição, ano de lançamento, classificação etária, duração e categorias.

---

## 🛠️ Ferramentas utilizadas

- Python
- pandas
- Matplotlib

---

## 🔎 Principais descobertas

### 1. Shows por país

![Gráfico de shows por país](images/top10-paises-shows.png)

> Conclusão: O catálogo da Netflix de 2000 a 2020 é imensamente dominado pelos Estados Unidos, com uma quantidade de shows muito superior a qualquer país, mais do que o triplo do segundo colocado, a Índia. É importante destacar que aqueles títulos cujo país de origem não estava especificado no dataset original foram excluídos desta análise, já que "país desconhecido" não representa uma categoria geográfica real.

---

### 2. Shows mais antigos e recentes por país

![Gráfico de shows mais antigos e recentes por país](images/datas-antigo-recente-top5.png)

>Conclusão: Entre os cinco países com mais shows no catálogo, os títulos mais recentes adicionados ficam concentrados perto de 2021-2022 para todos eles, o que mostra que a Netflix continua alimentando o catálogo desses países de forma parecida e constante. Já os títulos mais antigos variam bem mais: os Estados Unidos têm presença no catálogo desde 2008, enquanto o Canadá só aparece com força a partir de 2014. Essa análise foi feita com uma amostra dos 5 países com mais shows (os mesmos da pergunta anterior), já que representar todos os mais de 100 países no mesmo gráfico deixaria a visualização poluída e difícil de interpretar.

---

### 3. Diretores com mais filmes 

![Gráfico de diretores com mais filmes](images/top10-diretores.png)

>Conclusão: Rajiv Chilaka lidera o ranking de diretores com mais filmes na Netflix, com 22 títulos. Um número bem próximo dos segundos colocados, Jan Suter (21) e Raúl Campos (19), diferente do que aconteceu na análise por país, onde havia uma disparidade grande entre o primeiro e os demais. Essa análise considerou apenas filmes (não séries) e desconsiderou títulos sem diretor listado no dataset original.

---

## 📁 Estrutura do projeto
```
├── data/ # dataset original (CSV)
├── images/ # gráficos gerados pela análise
├── notebook/ # código da análise (formato #%%)
└── README.md
