# ATV_import 

Atividade n°01

Cria uma pasta temporária no computador chamada ATV_import
Dentro dela, cria um arquivo chamado main.py.
Dentro dessa mesma pasta, crie uma subpasta chamada ferramentas.
Dentro da pasta ferramentas, crie um arquivo chamado cripto.py.
No arquivo cripto.py, crie uma função simples em Python que apenas dê um print("Chave gerada com sucesso!").
Agora, abra o seu main.py e tente escrever a lógica de importação usando a Forma B (from ... import ...) para puxar aquela função de dentro da pasta ferramentas e executá-la.
Execute o main.py no seu terminal.

--- 

# ATV_Módulos

Atividade n°02
Construir o script teste_energia.py seguindo as instruções abaixo:

Passo 1: O Molde (A Classe)
Crie uma classe chamada ModuloConectado.
No construtor (__init__), ela deve receber e salvar no self três informações: nome (texto), status (booleano: True para ligado, False para desligado) e consumo (número flutuante representando Watts).

Passo 2: Os Objetos Independentes
Fora da classe, crie três objetos (três módulos diferentes) usando esse mesmo molde:
Um módulo de Wi-Fi, que nasce Ligado (True) e consome 1.5W.
Um módulo de NFC, que nasce Desligado (False) e consome 0.5W.
Um módulo de Sub-GHz, que nasce Ligado (True) e consome 1.2W.

Passo 3: A Caixa de Ferramentas (A Lista)
Crie uma lista chamada hardware_detectado e coloque os três objetos que você criou dentro dela usando colchetes [].

Passo 4: A Lógica do Diagnóstico (O Desafio)
Agora vem a parte onde você vai testar sua lógica. Escreva um código no final do arquivo que faça o seguinte:
Usando colchetes [] e o ponto ., dê um print direto no terminal exibindo apenas o nome do segundo módulo da sua lista (o NFC).
Crie uma variável chamada energia_total = 0. Usando um loop for para percorrer a sua lista de hardware, verifique se o módulo está ligado (status == True). Se ele estiver ligado, some o consumo dele na variável energia_total.
No final, dê um print exibindo o valor da energia_total calculada.