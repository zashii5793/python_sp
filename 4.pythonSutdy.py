class Michael:
    def __init__(self, max = 5, count = 0):
        self.max = max
        self.count = count

    def get_max(self):
        return self.__max

    def get_count(self):
        return self.__count 

    def set_max(self, max):
        self.__max = max

    def set_count(self,  count):
        self.__count = count           

    max = property(get_max, set_max)
    count = property(get_count, set_count)    

    def teach(self):
        if self.count < self.max:
            print('もっと強く')
        else:
            print('よっしオッケーだ')
        self.count += 1


oni = Michael()
oni.count = 2

for i in range(5):
    print('スマッシュ')
    oni.teach()