# src/__init__.py

# Importar módulos que serão usados frequentemente
from .data_cleaning import load_data, clean_data, save_data
from .features import calculate_kpis, print_kpis
from .utils import plot_correlation_matrix, plot_distribution, plot_histogram

# Inicialização de variáveis ou configuração
__version__ = "1.0.0"

print("Pacote de Análise de Locações de Veículos carregado!")