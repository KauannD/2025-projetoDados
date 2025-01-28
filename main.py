# main.py

import os
import pandas as pd
from src.data_cleaning import load_data, clean_data, save_data
from src.features import calculate_kpis, print_kpis
from src.models import train_model
from src.utils import plot_correlation_matrix, plot_distribution, plot_histogram

def main():
    raw_data_path = os.path.join("data", "raw", "MOCK_DATA.csv")
    processed_data_path = os.path.join("data", "processed", "dados_limpos.csv")
    
    # Carregar e limpar dados
    df = load_data(raw_data_path)
    df_clean = clean_data(df)
    save_data(df_clean, processed_data_path)
    
    # Calcular e imprimir KPIs
    kpis = calculate_kpis(df_clean)
    print_kpis(kpis)
    
    # Visualizações
    plot_correlation_matrix(df_clean)
    plot_distribution(df_clean, 'veiculo_marca', 'Distribuição de Locações por Marca de Veículo', 'Marca de Veículo', 'Contagem', 'distribuicao_por_marca.png')
    plot_distribution(df_clean, 'mes_locacao', 'Distribuição de Locações por Mês', 'Mês', 'Contagem', 'distribuicao_por_mes.png')
    plot_histogram(df_clean, 'avaliacao_veiculo', 'Distribuição das Avaliações dos Veículos', 'Avaliação', 'Frequência', 'distribuicao_avaliacoes_veiculos.png')
    plot_histogram(df_clean, 'avaliacao_atendimento', 'Distribuição das Avaliações do Atendimento', 'Avaliação', 'Frequência', 'distribuicao_avaliacoes_atendimento.png')
    
    # Modelagem
    X = df_clean[['mes_locacao', 'veiculo_ano', 'valor_diaria']]
    y = df_clean['tempo_locacao']
    model, mse, r2 = train_model(X, y)
    
    print(f"\nErro Quadrático Médio: {mse:.2f}")
    print(f"Coeficiente de Determinação (R^2): {r2:.2f}")

if __name__ == "__main__":
    main()