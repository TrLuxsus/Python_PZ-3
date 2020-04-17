class Worker:
    age = 0
    name = ""
    __weight = 0

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


#Test script
def main():
    wrk1 = Worker ()
    wrk1.age = 34
    wrk1.name = "Иванов"

    wrk1.eat(2)
    wrk1.eat(3)
    wrk1.eat(15)
    ves = wrk1.get_weight()

    print(wrk1, wrk1.age, wrk1.name, ves)


if __name__ == "__main__":
    main()
