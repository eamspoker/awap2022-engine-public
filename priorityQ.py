class pq():
    def __init__(self):
        self.list = []
        self.max = 0
        return
    
    def pq_insert(self, item):
        self.list.append(item)
    
    def pq_pop(self):
        index = 0
        for i in range(len(self.list)):
            if((self.list[i])[3] > self.max):
                self.max = (self.list[i])[3]
                index = i
        return self.list[index]


