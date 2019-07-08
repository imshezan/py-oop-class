class details:
    __fname=""
    __lname=""
    __gender=""
    __city=""
    __phone=0

    def ask(self):
        self.__fname = input("Enter First Name\t:")
        self.__lname = input("Enter Last Name\t:")
        self.__gender = input("Enter Gender:")
        self.__city = input("Enter City\t:")
        self.__phone = int(input("Enter Phone No:"))
    def view(self):
        print("Name\t:", self.__fname," ", self.__lname )
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Phone\t:", self.__phone)


def main():
    
    my=details()
    my.ask()
    my.view()

if __name__=="__main__":
    main()


