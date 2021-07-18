class Micheal:
    count = 0
    max = 5

    def teach(self):
        if self.__class__.count < self.__class__.max:
            print("もっと強く")
        else:
            print("OK") 
        self.__class__.count += 1


onil = Micheal()
for i in range(4):
    print("スマッシュ")
    onil.teach()

