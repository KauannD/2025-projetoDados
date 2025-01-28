import os
import tkinter as tk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv
from src.data_cleaning import load_data, clean_data, save_data
from src.features import calculate_kpis, print_kpis
from src.utils import plot_correlation_matrix, plot_distribution, plot_histogram

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Análise de Locações de Veículos")
        
        self.create_widgets()

    def create_widgets(self):
        # Botão para carregar dados
        self.load_button = tk.Button(self.root, text="Carregar Dados", command=self.load_data)
        self.load_button.pack(pady=10)

        # Botão para limpar dados
        self.clean_button = tk.Button(self.root, text="Limpar Dados", command=self.clean_data)
        self.clean_button.pack(pady=10)

        # Botão para calcular KPIs
        self.kpi_button = tk.Button(self.root, text="Calcular KPIs", command=self.calculate_kpis)
        self.kpi_button.pack(pady=10)

        # Botão para visualizar dados
        self.visualize_button = tk.Button(self.root, text="Visualizar Dados", command=self.visualize_data)
        self.visualize_button.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.df = load_data(file_path)
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")

    def clean_data(self):
        if hasattr(self, 'df'):
            self.df_clean = clean_data(self.df)
            save_data(self.df_clean, os.path.join("data", "processed", "dados_limpos.csv"))
            messagebox.showinfo("Sucesso", "Dados limpos e salvos com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, carregue os dados primeiro.")

    def calculate_kpis(self):
        if hasattr(self, 'df_clean'):
            kpis = calculate_kpis(self.df_clean)
            print_kpis(kpis)
            messagebox.showinfo("Sucesso", "KPIs calculados com sucesso! Verifique o console para detalhes.")
        else:
            messagebox.showerror("Erro", "Por favor, limpe os dados primeiro.")

    def visualize_data(self):
        if hasattr(self, 'df_clean'):
            plot_correlation_matrix(self.df_clean)
            plot_distribution(self.df_clean, 'veiculo_marca', 'Distribuição de Locações por Marca de Veículo', 'Marca de Veículo', 'Contagem', 'distribuicao_por_marca.png')
            plot_distribution(self.df_clean, 'mes_locacao', 'Distribuição de Locações por Mês', 'Mês', 'Contagem', 'distribuicao_por_mes.png')
            plot_histogram(self.df_clean, 'avaliacao_veiculo', 'Distribuição das Avaliações dos Veículos', 'Avaliação', 'Frequência', 'distribuicao_avaliacoes_veiculos.png')
            plot_histogram(self.df_clean, 'avaliacao_atendimento', 'Distribuição das Avaliações do Atendimento', 'Avaliação', 'Frequência', 'distribuicao_avaliacoes_atendimento.png')
            messagebox.showinfo("Sucesso", "Visualizações geradas com sucesso! Verifique a pasta 'data/results'.")
        else:
            messagebox.showerror("Erro", "Por favor, limpe os dados primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()