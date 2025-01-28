import pandas as pd

def csv_para_xlsx(arquivo_csv, arquivo_xlsx):
    """
    Converte um arquivo CSV para XLSX.

    Args:
        arquivo_csv (str): Caminho para o arquivo CSV.
        arquivo_xlsx (str): Caminho para o arquivo XLSX de saída.
    """

    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv)

        # Salva o DataFrame como um arquivo Excel
        df.to_excel(arquivo_xlsx, index=False)
        print(f"Arquivo CSV convertido para XLSX com sucesso: {arquivo_xlsx}")

    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {arquivo_csv}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
csv_file = "MOCK_DATA.csv"
excel_file = "meu_arquivo.xlsx"
csv_para_xlsx(csv_file, excel_file)