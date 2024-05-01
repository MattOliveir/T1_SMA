class SimpleQueue:
    def __init__(self, label, N_servers, limit, arrival_schedule, service_Schedule, network):
        self.label = label
        self.N_servers = N_servers
        self.limit = limit
        self.clients = 0
        self.arrival_schedule = arrival_schedule
        self.service_Schedule = service_Schedule
        self.timeAtService = [0] * (limit+1)
        self.losses = 0
        self.network = network