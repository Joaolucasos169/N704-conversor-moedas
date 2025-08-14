# ----- Closure -----
def criar_conversor(taxa_origem, taxa_destino):
    def converter(valor):
        return valor * (taxa_destino / taxa_origem)
    return converter

# ----- Função de alta ordem -----
def aplicar_funcao_extra(funcao, extra_func):
    def nova_funcao(valor):
        return extra_func(funcao(valor))
    return nova_funcao

# ----- Taxas fictícias -----
taxas = {
    "BRL": 1.0,   # Real
    "USD": 5.0,   # Dólar 
    "EUR": 6.0,   # Euro 
    "GBP": 7.0    # Libra 
}

# ----- Lambda para arredondamento -----
arredondar = lambda x: round(x, 2)

def converter_valor(moeda_origem, moeda_destino, valor):
    """Função pura para facilitar testes."""
    if moeda_origem not in taxas or moeda_destino not in taxas:
        raise ValueError("Moeda inválida.")
    if valor < 0:
        raise ValueError("Valor não pode ser negativo.")
    conversor = criar_conversor(taxas[moeda_origem], taxas[moeda_destino])
    return aplicar_funcao_extra(conversor, arredondar)(valor)

def gerar_tabela(moeda_origem, valor):
    """Gera dict {moeda_destino: valor_convertido} para todas as moedas."""
    tabela = {}
    for moeda in taxas.keys():
        conv = criar_conversor(taxas[moeda_origem], taxas[moeda])
        tabela[moeda] = arredondar(conv(valor))
    return tabela

def main():
    print("💱 Conversor de Moedas - N704 Programação Funcional")
    print("Moedas disponíveis:", ", ".join(taxas.keys()))

    moeda_origem = input("Digite a moeda de origem: ").strip().upper()
    if moeda_origem not in taxas:
        print("Moeda inválida!")
        return

    try:
        valor = float(input("Digite o valor: ").replace(",", "."))
    except ValueError:
        print("Valor inválido! Digite um número (ex.: 123.45).")
        return

    if valor < 0:
        print("Valor não pode ser negativo.")
        return

    moeda_destino = input("Digite a moeda de destino: ").strip().upper()
    if moeda_destino not in taxas:
        print("Moeda inválida!")
        return

    if moeda_origem == moeda_destino:
        print(f"\n💹 {valor} {moeda_origem} = {arredondar(valor)} {moeda_destino}")
    else:
        resultado = converter_valor(moeda_origem, moeda_destino, valor)
        print(f"\n💹 {valor} {moeda_origem} = {resultado} {moeda_destino}")

    # ----- Tabela de conversões (corrigida) -----
    print("\n📊 Tabela de conversões para todas as moedas:")
    tabela = gerar_tabela(moeda_origem, valor)
    for moeda, valor_conv in tabela.items():
        print(f"{moeda}: {valor_conv}")
        
if __name__ == "__main__":
    main()
