import json

# Dados de entrada
segmento = "Serviços em geral"
cargo = "Analista"
licencas = "4 a 8"

# Pontuação por categoria
segmentos = {
    "Software e Cloud": 15,
    "Comércio": 13,
    "Serviços em geral": 11,
    "Serviços e Estética": 9,
    "Indústria Geral": 7,
    "Financeiro e Serviços Relacionados": 5
}
cargos = {
    "Gerente": 15,
    "Diretor": 13,
    "Analista": 11,
    "Coordenador": 9,
    "Supervisor": 7,
    "Assistente": 5
}
licencas_pontuacao = {
    "1 a 3": 10,
    "4 a 8": 30,
    "9 a 15": 50,
    "Acima de 15": 70
}

# Pesos
pesos = {
    "segmento": 0.15,
    "cargo": 0.15,
    "licencas": 0.70
}

# Cálculo
seg_score = segmentos.get(segmento, 3)
cargo_score = cargos.get(cargo, 3)
licenca_score = licencas_pontuacao.get(licencas, 10)

score_total = (
    (seg_score / 15) * pesos["segmento"] * 100 +
    (cargo_score / 15) * pesos["cargo"] * 100 +
    (licenca_score / 70) * pesos["licencas"] * 100
)

# Classificação
if score_total <= 20:
    classificacao = "Lead Frio"
elif score_total <= 50:
    classificacao = "Lead Morno"
elif score_total <= 80:
    classificacao = "Lead Quente"
else:
    classificacao = "Lead Muito Quente"

print(json.dumps({
    "lead_score": round(score_total, 2),
    "classificacao": classificacao
}))
' | python3
