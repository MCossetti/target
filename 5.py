# Definindo a string a ser invertida
string = "target sistemas"

# Inicializando uma variável para armazenar a string invertida
string_invertida = ""

# Iterando sobre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    # Adicionando cada caractere à variável string_invertida
    string_invertida += string[i]

# Exibindo a string invertida
print("String original:", string)
print("String invertida:", string_invertida)
