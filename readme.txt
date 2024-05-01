INTEGRANTES: ALEXYA OLIVEIRA, ADRIANA SERPA, VITTORIA PRESA, MATHEUS OLIVEIRA.


Instruções para Executar o Simulador
Para executar o simulador, siga os passos abaixo:

Configuração dos Parâmetros:
Abra o arquivo de configuração chamado "config.ini".
Dentro do arquivo, ajuste os parâmetros da simulação seguindo o padrão abaixo:

[configfile]
initial_Time: [["q1", 2]]
quantity_Nums: 100000
seed: 123
#label, N_servers, lmit, arrival_schedule, service_Schedule, network
queuesList: [["q1", 1, inf, [2, 4], [1, 2], [["q2", 0.8], ["q3", 0.2]]], ["q2", 2, 5, -1, [4, 8], [["q1", 0.3], ["q2", 0.5]]], ["q3", 2, 10, -1, [5, 15], [["q3", 0.7]]]]


Ajuste os parâmetros conforme necessário, incluindo o tempo inicial em que chega o primeiro cliente em cada fila, a quantidade de números aleatórios a serem gerados e a semente para os números aleatórios.
Na lista "queuesList", defina as características de cada fila da rede de filas, seguindo a ordem de atributos especificada.


Execução do Simulador através de uma IDE:

Configure o Arquivo "Config.ini" e salve.

Abra um terminal e rode o arquivo "app.py".



Execução do Simulador pelo Terminal:

Configure o Arquivo "Config.ini" e salve.

Abra um terminal na pasta do projeto e rode o comando "python app.py".