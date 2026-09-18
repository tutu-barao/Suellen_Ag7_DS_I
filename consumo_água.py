# Agenda 7 - Classificação de Consumo de Água
# Suellen Melquiades Campos

def classificar_consumo(tipo_imovel, consumo_mensal):
    """
    Função responsável por processar a regra de negócio
    e retornar a mensagem de alerta correspondente.
    """
    tipo_imovel = tipo_imovel.lower().strip()
    
    if tipo_imovel == "comercial":
        return "Tarifa comercial aplicada – consulte o plano corporativo."
    elif tipo_imovel == "apartamento" and consumo_mensal < 10:
        return "Consumo econômico – excelente controle de água!"
    elif (tipo_imovel == "apartamento" and consumo_mensal >= 10) or (tipo_imovel == "casa" and consumo_mensal <= 25):
        return "Consumo moderado – dentro do padrão residencial."
    else:
        return "Consumo excessivo – adote medidas de economia e verifique vazamentos."


#Dados de Entrada:
print("=== Sistema de Classificação de Consumo de Água ===")
tipo_imovel = input("Digite o tipo do imóvel (comercial, casa, apartamento): ")
consumo_mensal = float(input("Digite o consumo mensal de água em m³: "))

# Processamento e Saída
resultado = classificar_consumo(tipo_imovel, consumo_mensal)
print(f"\nResultado: {resultado}")
