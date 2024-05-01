from randomNumberGen import Generated_Numbers
from Queue import SimpleQueue

class Simulation:
    def __init__(self, initial_Time, quantity_Nums, seed, queuesList):
        self.time = 0
        self.initial_Event_Time = initial_Time
        self.nums = Generated_Numbers(quantity_Nums, seed)
        self.used_Nums = 0
        self.quantity_Nums = quantity_Nums
        self.queues_List = queuesList
        self.losses = 0
        self.scheduler = []
        self.events = []

    #Consume RNG
    def convert(self, a, b):
        result = (b-a)*self.nums.getNums()[self.used_Nums]+a
        self.used_Nums+=1
        return result

    #Schedule/Draw
    def putSchedule(self, event, q1, q2):
        if self.used_Nums>=self.quantity_Nums:
            print('USED ALL RNDNUMS')
            return
        
        #Draw

        if event == 'ch1':
            eventTime = round(self.convert(q1.arrival_schedule[0],q1.arrival_schedule[1]) + self.time,4) 
            schedule = {'event': event, 'time': eventTime, 'queue': q1}
        if event == 'p12':
            eventTime = round(self.convert(q1.service_Schedule[0], q1.service_Schedule[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue1': q1, 'queue2': q2}
        if event == 'sa2':
            eventTime = round(self.convert(q1.service_Schedule[0],q1.service_Schedule[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': q1}
        self.scheduler.append(schedule)
        #sort Scheduler
        self.scheduler = sorted(self.scheduler, key=lambda x: float(x['time']))

    #function to start the simulation
    
    def execute(self):
        #Scheduler

        for queue in self.queues_List:
            for time in self.initial_Event_Time:
                if time[0] == queue.label:
                    firstSchedule = {'event': 'ch1', 'time': time[1], 'queue': queue}
                    self.scheduler.append(firstSchedule)
        self.scheduler = sorted(self.scheduler, key=lambda x: float(x['time']))    

        while(self.used_Nums<self.quantity_Nums):

            #LowerTime
            event = self.scheduler.pop(0)

            e, tm, qe1, qe2, qe = 'event', 'time', 'queue1', 'queue2', 'queue'
            if event.get('event') == 'p12':
                print(f'event: {event.get(e)}, time: {event.get(tm)}, queue1: {event.get(qe1).label}, queue2: {event.get(qe2).label}, {event.get(qe1).clients}, {event.get(qe2).clients}', end='\n\n')
            else:
                print(f'event: {event.get(e)}, time: {event.get(tm)}, queue: {event.get(qe).label}, {event.get(qe).clients}', end='\n\n')

            #Time for Queue

            for queue in self.queues_List:
                queue.timeAtService[queue.clients]=round(queue.timeAtService[queue.clients] + event.get('time')-self.time,4)
                

            self.time = event.get('time')
            if event.get('event') == 'ch1':
                self.ch1(event.get('queue'))
            if event.get('event') == 'p12':
                self.p12(event.get('queue1'), event.get('queue2'))
            if event.get('event') == 'sa2':
                self.sa2(event.get('queue'))

    def checkDestination(self, q, prob):
        aux = 0
        for dest in q.network:
            aux+=dest[1]
            if prob <= aux:
                print(dest[0])
                return dest[0]
        return 's'

    def scheduleDest(self, q, d):
        if d == 's':
            self.putSchedule('sa2', q, -1)
        else:
            q2 = ''
            for q0 in self.queues_List:
                if q0.label == d:
                    q2 = q0
            self.putSchedule('p12', q, q2)

    #Arrive
    def ch1(self, q):
        if q.clients<q.limit:
            q.clients+=1
            if q.clients<=q.N_servers:
                #Target
                if self.used_Nums>=self.quantity_Nums:
                    print('USED ALL RNDNUMS')
                    return
                self.scheduleDest(q, self.checkDestination(q, self.convert(0,1)))
        else:
            self.losses+=1
            q.losses+=1
        self.putSchedule('ch1', q, -1)#Arrive
    
    #Change Queue
    def p12(self, q1 , q2):
        q1.clients-=1
        if q1.clients>=q1.N_servers:
            if self.used_Nums>=self.quantity_Nums:
                print('USED ALL RANDOM NUMBERS')
                return
            self.scheduleDest(q1, self.checkDestination(q1, self.convert(0,1)))
        if q2.clients<q2.limit:
            q2.clients+=1
            if q2.clients<=q2.N_servers:
                if self.used_Nums>=self.quantity_Nums:
                    print('USED ALL RANDOM NUMBERS')
                    return
                self.scheduleDest(q2, self.checkDestination(q2, self.convert(0,1)))
        else:
            self.losses+=1
            q2.losses+=1

    #Leave Queue
    def sa2(self, q):
        q.clients-=1
        if q.clients>=q.N_servers:
            if self.used_Nums>=self.quantity_Nums:
                print('USED ALL RANDOM NUMBERS')
                return
            self.scheduleDest(q, self.checkDestination(q, self.convert(0,1)))