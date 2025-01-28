# src/data_cleaning.py

import pandas as pd
import os


def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def clean_data(df):
    # Limpeza dos dados
    df = df.dropna()
    df = df.drop_duplicates()
    df = df[(df['veiculo_ano'] <= 2025) & (df['veiculo_ano'] >= 1995)]
    df['data_locacao'] = pd.to_datetime(df['data_locacao'])
    df['data_devolucao'] = pd.to_datetime(df['data_devolucao'])
    df['ano_locacao'] = df['data_locacao'].dt.year
    df['mes_locacao'] = df['data_locacao'].dt.month
    return df

if __name__ == "__main__":
    raw_data_path = os.path.join("data", "raw", "MOCK_DATA.csv")
    processed_data_path = os.path.join("data", "processed", "dados_limpos.csv")
    
    df = load_data(raw_data_path)
    df_clean = clean_data(df)
    save_data(df_clean, processed_data_path)
    print(f"\nDataFrame limpo salvo em '{processed_data_path}'")