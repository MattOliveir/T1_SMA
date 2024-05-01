from simulation import Simulation
from Queue import SimpleQueue
from array import array
import configparser

inf = 999999
#read configuration file
config = configparser.ConfigParser()
config.read("config.ini")
initial_Time = eval(config.get("config", "initial_Time"))
quantity_Nums = int(config.get("config", "quantity_Nums"))
seed = int(config.get("config", "seed"))
#get queue
#get filas
queuesListArr = eval(config.get("config", "queuesList"))
queuesListObj = []

for q in queuesListArr:
    q[5].sort(key = lambda x:x[1])
    simQueue = SimpleQueue(q[0], q[1], q[2], q[3], q[4], q[5])
    queuesListObj.append(simQueue)


#instanciacao e start da simulacao
sim = Simulation(initial_Time, quantity_Nums, seed, queuesListObj)
sim.execute()

for queue in sim.queues_List:
    print(f'Fila: {queue.label}')
    
    max = 0
    for index in range(len(queue.timeAtService)):

        

        if max < 10:        
            print(f'Estado: {index}, Tempo: {queue.timeAtService[index]}, Probabilidade: {round((queue.timeAtService[index]/sim.time)*100,4)}%')
        else:
            break
        max += 1

    print(f'Perdas: {queue.losses}')
print(f'Tempo da Simulação: {sim.time}')
print(f'Total Perdas: {sim.losses}')
input()