# Atividade n°02
# Construir o script teste_energia.py seguindo as instruções abaixo:

# Passo 1: O Molde (A Classe)
# Crie uma classe chamada ModuloConectado.
# No construtor (__init__), ela deve receber e salvar no self três informações: nome (texto), status (booleano: True para ligado, False para desligado) e consumo (número flutuante representando Watts).

# Passo 2: Os Objetos Independentes
# Fora da classe, crie três objetos (três módulos diferentes) usando esse mesmo molde:
# Um módulo de Wi-Fi, que nasce Ligado (True) e consome 1.5W.
# Um módulo de NFC, que nasce Desligado (False) e consome 0.5W.
# Um módulo de Sub-GHz, que nasce Ligado (True) e consome 1.2W.

# Passo 3: A Caixa de Ferramentas (A Lista)
# Crie uma lista chamada hardware_detectado e coloque os três objetos que você criou dentro dela usando colchetes [].


# Passo 4: A Lógica do Diagnóstico (O Desafio)
# Agora vem a parte onde você vai testar sua lógica. Escreva um código no final do arquivo que faça o seguinte:
# Usando colchetes [] e o ponto ., dê um print direto no terminal exibindo apenas o nome do segundo módulo da sua lista (o NFC).
# Crie uma variável chamada energia_total = 0. Usando um loop for para percorrer a sua lista de hardware, verifique se o módulo está ligado (status == True). Se ele estiver ligado, some o consumo dele na variável energia_total.
# No final, dê um print exibindo o valor da energia_total calculada.
acum = 0.0


class ModuloConectado:
    def __init__(self, nome, status, consumo):
        self.nome = str(nome)
        self.status = bool(status)
        self.consumo = float(consumo)


modulo_wifi = ModuloConectado("wifi", True, 1.5)
modulo_nfc = ModuloConectado("nfc", False, 0.5)
modulo_subghz = ModuloConectado("subghz", True, 1.2)

hardware_detectado = [modulo_wifi, modulo_nfc, modulo_subghz]

for modulo in hardware_detectado:
    if modulo.status == True:
        acum = acum + modulo.consumo

print(acum, "W")
