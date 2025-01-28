# src/utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

def save_plot(fig, filename):
    results_dir = os.path.join("data", "results")
    os.makedirs(results_dir, exist_ok=True)
    fig.savefig(os.path.join(results_dir, filename))
    plt.close(fig)

def plot_correlation_matrix(df):
    # Selecionar apenas as colunas numéricas
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Matriz de Correlação')
    save_plot(fig, 'matriz_correlacao.png')

def plot_distribution(df, column, title, xlabel, ylabel, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x=column, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45)
    save_plot(fig, filename)

def plot_histogram(df, column, title, xlabel, ylabel, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=10, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_plot(fig, filename)