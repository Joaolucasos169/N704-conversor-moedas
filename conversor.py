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

def main():
    print("💱 Conversor de Moedas - N704 Programação Funcional")
    print("Moedas disponíveis:", ", ".join(taxas.keys()))

    moeda_origem = input("Digite a moeda de origem: ").upper()
    if moeda_origem not in taxas:
        print("Moeda inválida!")
        return

    valor = float(input("Digite o valor: "))

    moeda_destino = input("Digite a moeda de destino: ").upper()
    if moeda_destino not in taxas:
        print("Moeda inválida!")
        return

    # Criar closure para conversão direta
    conversor = criar_conversor(taxas[moeda_origem], taxas[moeda_destino])

    # Função de alta ordem aplicando arredondamento
    conversor_com_arredondamento = aplicar_funcao_extra(conversor, arredondar)

    resultado = conversor_com_arredondamento(valor)
    print(f"\n💹 {valor} {moeda_origem} = {resultado} {moeda_destino}")

    # ----- List comprehension -----
    print("\n📊 Tabela de conversões para todas as moedas:")
    tabela = [
        f"{moeda}: {arredondar(conversor(valor * (taxas[moeda_origem] / taxas[moeda]), ))}"
        for moeda in taxas.keys()
    ]
    print("\n".join(tabela))

if __name__ == "__main__":
    main()
