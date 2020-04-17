class Worker:
    age = 0
    name = ""
    __weight = 0

    def eat (self, how_much):
        self.__weight += how_much

    def get_weight(self):
        return self.__weight


def main():
    wrk1 = Worker ()
    wrk1.age = 34
    wrk1.name = "Иванов"

    print(wrk1, wrk1.age, wrk1.name)


if __name__ == "__main__":
    main()