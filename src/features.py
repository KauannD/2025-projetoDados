# src/features.py

def calculate_kpis(df):
    receita_total = df['valor_total'].sum()
    tempo_medio_locacao = df['tempo_locacao'].mean()
    distribuicao_pagamento = df['forma_pagamento'].value_counts(normalize=True) * 100
    status_locacao = df['status_locacao'].value_counts()
    return {
        "receita_total": receita_total,
        "tempo_medio_locacao": tempo_medio_locacao,
        "distribuicao_pagamento": distribuicao_pagamento,
        "status_locacao": status_locacao
    }

def print_kpis(kpis):
    print(f"\nReceita Total: R${kpis['receita_total']:.2f}")
    print(f"Tempo Médio de Locação: {kpis['tempo_medio_locacao']:.2f} dias")
    print("\nDistribuição por Forma de Pagamento:")
    print(kpis['distribuicao_pagamento'])
    print("\nQuantidade de Locações por Status:")
    print(kpis['status_locacao'])