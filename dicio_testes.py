import excel

moedas = {'JPY': 5000.0, 'GBP': 3550.0, 'CAD': 1400.0} #dicionario moeda com a quantidade
acoes = {'PINS': 100.0, 'VALE': 274.0, 'NFLX': 20.0} #dicionario acao com quantidade
moedas_cota = {'JPY': 0.04, 'GBP': 5.95, 'CAD': 3.71}#dicionario cotacao moedda em relação ao real
acoes_cota = {'PINS': 96.11, 'VALE': 85.02, 'NFLX': 917.39}#dicionario cotacao acao em relação ao real

excel.planilha(moedas, acoes, moedas_cota, acoes_cota)
