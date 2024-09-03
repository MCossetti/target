import json

# Função para carregar dados do JSON
def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Função para calcular o menor, maior valor de faturamento e dias com faturamento acima da média
def analyze_faturamento(data):
    # Filtrar dias com faturamento > 0
    valid_faturamento = [item['valor'] for item in data if item['valor'] > 0]
    
    # Calcular menor e maior valor de faturamento
    min_faturamento = min(valid_faturamento)
    max_faturamento = max(valid_faturamento)
    
    # Calcular média mensal
    media_mensal = sum(valid_faturamento) / len(valid_faturamento)
    
    # Contar dias com faturamento acima da média mensal
    days_above_average = sum(1 for valor in valid_faturamento if valor > media_mensal)
    
    return min_faturamento, max_faturamento, days_above_average

# Carregar dados do JSON
data = load_data_from_json("../target/3/dados.json")

# Analisar faturamento
min_faturamento, max_faturamento, days_above_average = analyze_faturamento(data)

# Exibir resultados
print(f"Menor valor de faturamento: {min_faturamento}")
print(f"Maior valor de faturamento: {max_faturamento}")
print(f"Número de dias com faturamento acima da média: {days_above_average}")
