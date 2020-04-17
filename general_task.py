class Worker:
    age = 0
    name = ""
    __weight = 0
    __mood = 10

    #Method eat increaces weight of the worker 
    #if eaten maore than 10 kgs weight increased in half and age increased by 1
    def eat(self, how_much):
        if how_much > 10:
            self.age += 1
            self.__weight += how_much / 2
        else:
            self.__weight += how_much

    #Get weight of the worker
    def get_weight(self):
        return self.__weight

    #Increase mood by 1
    def walk(self):
        self.__mood += 1
    
    #Increase mood by 2
    def dance(self):
        self.__mood += 2

    #Reduce mood by 2
    def work(self):
        self.__mood -= 2

    #Get mood of the worker
    def get_mood(self):
        return self.__mood


#Test script
def main():
    wrk1 = Worker ()
    wrk1.age = int(input("Enter worker age:"))
    wrk1.name = input("Enter worker name:")

    wrk1.eat(2)
    wrk1.eat(3)
    wrk1.eat(15)
    ves = wrk1.get_weight()

    wrk1.walk()
    wrk1.walk()
    wrk1.walk()
    wrk1.dance()

    for i in range(1, 9):
        wrk1.work()

    print(wrk1, wrk1.age, wrk1.name, ves, wrk1.get_mood())


if __name__ == "__main__":
    main()
