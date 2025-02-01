# Projeto de Análise de Locações de Veículos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0%2B-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2%2B-blue)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24.2%2B-blue)

## Visão Geral

Objetivo do projeto realiza a análise, visualização e modelagem preditiva dos dados de locações de veículos. O objetivo é fornecer insights sobre o desempenho do negócio, identificar padrões e tendências.

## Estrutura do Projeto


```plaintext
projeto/
├── data/
│   ├── raw/              # Dados brutos
│   ├── processed/        # Dados processados
│   └── results/          # Resultados das análises
├── interface/
│   └── interface.py      # Interface gráfica do usuário
├── notebooks/
│   └── analise_locacoes.ipynb  # Notebooks Jupyter para análises exploratórias
├── src/
│   ├── __init__.py       # Arquivo indicador de pacote
│   ├── data_cleaning.py  # Funções para limpeza de dados
│   ├── features.py       # Funções para cálculo de KPIs
│   ├── models.py         # Modelos de machine learning (se aplicável)
│   └── utils.py          # Funções utilitárias para visualização e outras tarefas
├── pyproject.toml        # Arquivo de configuração do Poetry
├── poetry.lock           # Arquivo de lock do Poetry
├── main.py               # Script principal do projeto
└── README.md             # Documentação do projeto

```

### Funcionalidades
- Carregamento e Limpeza de Dados: Carrega os dados brutos e realiza a limpeza e pré-processamento.
- Cálculo de KPIs: Calcula indicadores-chave de desempenho, como receita total, tempo médio de locação, distribuição por forma de pagamento, etc.
- Visualizações: Gera gráficos e visualizações para explorar os dados e identificar padrões e tendências.
- Modelagem Preditiva: Constrói e avalia modelos preditivos para prever a demanda futura e outros aspectos do negócio.

### Instalação
```plaintext
Pré-requisitos
Python 3.10+
Poetry (para gerenciamento de dependências)
```

### Passos para Instalação
```plaintext
Clone o repositório:

bash
git clone https://github.com/KauannD/projeto_data_science.git
cd projeto_data_science
Instale as dependências usando o Poetry:

bash
poetry install
Utilização
Executando o Script Principal
Para executar o script principal e realizar toda a análise e modelagem, use o seguinte comando:

bash
poetry run python main.py
Utilizando o Notebook Jupyter
Para executar o notebook Jupyter e realizar a análise de forma interativa, use o seguinte comando:

bash
poetry run jupyter notebook
Abra o arquivo analise_locacoes.ipynb e execute as células conforme necessário.
```

***Estrutura dos Arquivos***
```plaintext
src/data_cleaning.py
Contém funções para carregar, limpar e salvar os dados.

load_data(file_path): Carrega os dados a partir de um arquivo CSV.
clean_data(df): Limpa os dados carregados.
save_data(df, file_path): Salva os dados limpos em um arquivo CSV.
src/features.py
Contém funções para calcular KPIs.

calculate_kpis(df): Calcula os KPIs a partir dos dados limpos.
print_kpis(kpis): Imprime os KPIs calculados.
src/utils.py
Contém funções utilitárias para visualização de dados.

plot_correlation_matrix(df): Plota a matriz de correlação.
plot_distribution(df, column, title, xlabel, ylabel, output_file): Plota a distribuição de uma coluna específica.
plot_histogram(df, column, title, xlabel, ylabel, output_file): Plota o histograma de uma coluna específica.
Variáveis de Ambiente
Este projeto utiliza variáveis de ambiente armazenadas em um arquivo .env. Certifique-se de criar e configurar este arquivo conforme necessário.

- Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório.
```
## Uso

- Interface Gráfica
Para executar a interface gráfica, use o comando:
bash
poetry run python interface/interface.py
ou
PYTHONPATH=$(pwd) poetry run python interface/interface.py
Executar o Script Principal
Para executar o script principal do projeto:

bash
poetry run python main.py

## Contato
KauannD - [GitHub](https://github.com/KauannD)
