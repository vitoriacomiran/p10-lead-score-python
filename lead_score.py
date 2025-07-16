echo '
import json

# primeiro passo: definir as variáveis
segmentos = input("Informe os segmentos: ")
cargos = input("Informe o cargo: ")
qtd_licencas = int(input("Qual a quantidade de licenças: "))

# segundo passo: definir os valores das variáveis
pontos_segmentos = {
    "Software e Cloud" : 15,
    "Comércio" : 13,
    "Serviços em geral" : 11,
    "Serviços e Estética" : 9,
    "Indústria Geral" : 7,
    "Financeiro e Serviços Relacionados" : 5,
    "Outros" : 3
}

pontos_cargos = {
    "Gerente" : 15,
    "Diretor" : 13,
    "Analista" : 11,
    "Coordenador" : 9,
    "Supervisor" : 7,
    "Assistente" : 5,
    "Outros" : 3
}

pontos_licencas = {
    "1 a 3" : 10,
    "4 a 8" : 30,
    "9 a 15" : 50,
    "Acima de 15" : 70
}

# passo 3: definir o peso de cada etapa
pesos = {
    "segmentos": 0.15,
    "cargos": 0.15,
    "qtd_licencas": 0.70
}

#passo 4: definir o cálculo entre etapas e total
segmento_score = pontos_segmentos.get(segmentos, 3)
cargo_score = pontos_cargos.get(cargos, 3)
qtd_licencas_score = pontos_licencas.get(qtd_licencas, 10)

# verifica se o valor está no dicionário de segmentos, se não estiver ou for outro, atribui o valor de 3
# para o campo cargo a mesma coisa
# na licença caso no futuro inserimos um campo 'ainda não sei' ele pegaria os 10 pontos padrões

# passo 5: definir o cálculo do score final

score_total = (
    (segmento_score / 15) + pesos["segmentos"] +
    (cargo_score / 15) + pesos["cargos"] +
    (qtd_licencas_score / 70) + pesos["qtd_licencas"] * 100
)

# passo 6: definir o lead score final
if score_total <= 20:
    score = "Lead Frio"
elif score_total <= 50:
    score = "Lead Morno"
elif score_total <= 70:
    score = "Lead Quente"
else:
    score = "Lead Muito Quente"

# passo 7: printar o valor do score

print(json.dumps({"lead_score": round(score_total, 2), "score": score}))

'| python3
