from controllers.controller import Controller
import getpass
import sys

class Menu:
    def __init__(self):
        #self.name = name
        self.controller = Controller()
        self.__user_is_active = False
        self.user = False
        self.commands = {
            "show_movies": self.show_movies,
            "show_projections": self.show_projections,
            "make_reservations": self.make_reservations,
            "give_up": self.give_up,
            "register": self.register,
            "login": self.login,
            "finalize": self.finalize,
            "help": self.help,
            "exit": self.exit
        }


    def login(self, *args):
        username = input("Enter your name: ")
        password = getpass.getpass('Enter password:')
        self.user = self.controller.login(username, password)
        if self.user != False:
            self.__user_is_active = True
            print("You have loged in successfuly")
            return 

    def register(self, *args):
        username = input("Enter your name: ")
        password = getpass.getpass('Enter password:')
        self.controller.register(username, password)
        print("Registration successful. Now login")
        self.login()

    def show_movies(self, *args):
        print("Current movies:")
        print(self.controller.show_movies())

    def show_projections(self, movie_id, date=None):
        print(f"Projections for movie \'{self.controller.get_movie_name(movie_id)[0][0]}\':")
        print(self.controller.show_projections(movie_id, date))

    def make_reservations(self, *args):
        while not self.__user_is_active:
            self.login()
            if self.user == False:
                self.register()
        self.show_movies()
        movie_id = int(input("Enter movie id: "))
        self.show_projections(movie_id)
        projection_id = int(input("Enter projection id: "))
        print(self.controller.show_cinema_map(projection_id))
        number_of_tickets = int(input("Enter number of tickets: "))
        free_seats = self.controller.get_free_seats(projection_id)
        while free_seats < number_of_tickets:
            number_of_tickets = int(input(f"There are {free_seats} free seats. Enter number of tickets you want: "))
        for i in range(0, number_of_tickets):
            row = int(input("Enter row: "))
            col = int(input("Enter seat: "))
            self.controller.add_new_reservation(self.user[0], projection_id, row, col)
        print("If you want to finish your reservation type \"finalize\": ")

    def finalize(self, *args):
        self.controller.finalize()

    def give_up(self, *args):
        self.start()

    def help(self):
        pass

    def exit(self, *args):
        sys.exit()


    def start(self):
        print("Hello!")
        while True:
            command = ""
            parameter1 = None
            parameter2 = None

            user_input = input("Enter command: ")
            user_input = user_input.split()
            command = user_input[0]
            if len(user_input) > 1:
                parameter1 = user_input[1]
                if len(user_input) > 2:
                    parameter2 = user_input[2]

            self.commands[command](parameter1, parameter2)
