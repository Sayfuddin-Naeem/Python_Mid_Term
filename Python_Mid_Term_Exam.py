import re

# It is for text formating purpose
text_format = """        """

#Star Cinema Class Start
class Star_Cinema():
    __hall_list = []

    def __init__ (self, hall_obj)->None:
        self.__hall_list.append(hall_obj)
    
    @property
    def hall_list(self):
        return self.__hall_list

# Hall Class Start
class Hall(Star_Cinema):
    
    def __init__ (self, rows, cols, hall_no):
        super().__init__(self)
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
    
    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        self.__seats[show_id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def isValid(self,i, j):
        return (i>=0 and i < self.__rows) and (j>=0 and j < self.__cols)


    def book_seats(self, show_id, seatList):
        if show_id not in self.__seats:
            print(text_format+"Show_Id is not found! Insert a existing Show_Id.")
            return

        isAvailable = True
        print()
        for p in seatList:
            if self.isValid(p[0], p[1]):
                if self.__seats[show_id][p[0]][p[1]] == 0:
                    self.__seats[show_id][p[0]][p[1]] = 1
                    print(f"{text_format}Seat({p[0]}, {p[1]}) is booked for Show Id {show_id}")
                else:
                    isAvailable = False
                    print(f"{text_format}Seat({p[0]}, {p[1]}) is not available, select a available seat")
            else:
                print(f"{text_format}Insert valid row and column values of a seat.\n{text_format}Valid rows are 0 to {self.__rows} and columns are 0 to {self.__cols}")
        print()
        if not isAvailable:
            self.view_available_seats(show_id)
    
    def view_show_list(self):
        if not self.__show_list:
            print(text_format+"No shows are currently running.")
            return
        
        print('\n'+text_format+"\t\t----------------------------------")
        print(text_format+"\t\t\tList of Running show")
        print(text_format+"\t\t----------------------------------\n")
        for show in self.__show_list:
            print(f"{text_format}Movei Name: {show[1]}({show[0]}) Show Id: {show[0]} Time: {show[2]}")
        print()

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(text_format+"Show_Id is not found! Insert a existing Show_Id.")
            return
        
        ct = 0
        print('\n'+text_format+"\t\t----------------------------------")
        print(text_format+"\t\t\tAvailable Seat List")
        print(text_format+"\t\t----------------------------------\n")
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[show_id][i][j] == 0:
                    print(f"{text_format}Seat({i}, {j}) ", end="")
                    ct += 1
                if ct == 5:
                    print()
                    ct = 0
        print()


    

## Main Functionality Start Here
hall1 = Hall(8, 8, 101)
hall1.entry_show("110", "Jawan", "15/06/2024 6:00 PM")
hall1.entry_show("111", "Don", "15/06/2024 9:00 PM")
hall1.entry_show("112", "KGF", "17/06/2024 11:00 AM")
hall1.entry_show("113", "Dhoom", "17/06/2024 2:00 PM")
hall1.entry_show("114", "3 Idiots", "18/06/2024 10:00 AM")


options ="""
        1. VIEW ALL SHOW TODAY
        2. VIEW AVAILABLE SEATS
        3. BOOK TICKET
        4. EXIT
        Enter Option: """

def input_split(val):
    result = re.split(r'\D+', val)
    result = [int(x) for x in result if x]
    return result

def book_tickets():
    hall1.view_show_list()
    show_id = input(text_format+"ENTER SHOW ID: ")
    numTickets = int(input(text_format+"Number of Ticket??: "))
    seat_ls = []

    for i in range(1, numTickets+1):
        row, col = input_split(input(f"{text_format}Enter ticket-{i} seat's row and col(e.g. 4 5): "))
        seat_ls.append((row, col))

    hall1.book_seats(show_id, seat_ls)

while True:
    op = input(options)
    if op == "4":
        break
    elif op == "1":
        hall1.view_show_list()
    elif op == "2":
        s_id = input(text_format+"ETER SHOW ID: ")
        hall1.view_available_seats(s_id)
    elif op == "3":
        book_tickets()
        
    else:
        print("Invalid option! Enter a valid option")