class Worker:
    age = 0
    name = ""
    __weight = 0

    #Method eat increaces weight of the worker 
    def eat(self, how_much):
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
    ves = wrk1.get_weight()

    print(wrk1, wrk1.age, wrk1.name, ves)


if __name__ == "__main__":
    main()
