class Star_Cinema:
    hall_list = []

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        # id = input("Enter your id: ")
        # movie_name = input("Movie name: ")
        # time = input("Time: ")
        self.id = id
        self.movie_name = movie_name
        self.time = time

        showInfo = (self.id,self.movie_name,self.time)
        self.show_list.append(showInfo)

        self.arr = [[0 for i in range(self._cols)] for j in range(self._rows)]
        
        self.seats[id] = self.arr

        # print(self.seats[id])

    def book_seats(self):
        id = input("Enter your id: ")
        self.term = False
        for show in self.show_list:
            if show[0] == id:
                self.term = True
                seat_num = int(input("How many seats: "))
                for j in range(seat_num):
                    row = int(input("Enter your row: "))
                    col = int(input("Enter your column: "))

                    if (row > self._rows or col > self._cols) or (row < 0 or  col < 0):
                        print("enter valid number !!!\n") 
                    elif self.arr[row][col] == 1:
                        print("this seat is already booked \n")
                    else:
                        self.arr[row][col] = 1
                        if j == 0:
                            print("1st seat booked!!!\n")
                        elif j == 1:
                            print("2nd seat booked!!!\n")
                        elif j == 2:
                            print("3rd seat booked!!!\n")
                        else:
                            print(f"{j+1}th seat booked!!!\n")
        if self.term is False:
            print("This id is not available")
            print("please enter valid id !!\n")


    def view_show_list(self):
        for show in self.show_list:
            print(f"id: {show[0]} movie name: {show[1]}  Time: {show[2]}" )

    def view_available_seats(self):
        id = input("Enter id: ")
        self.yes = False
        for show in self.show_list:
            if show[0] == id:
                self.yes = True
                for row in self.seats[id]:
                    for elem in row:
                        print(elem, end=' ')
                    print()
        if self.yes == False:
            print("\nenter valid id !!\n")
        
            



blockbuster = Star_Cinema()

hall_1 = Hall(5,5,100)
hall_1.entry_show('111','jawan','11 am')
hall_1.entry_show('222','majhi','12 am')


while True:

    print("Options: \n")
    print("1 : view all show today")
    print("2 : view available seats")
    print("3 : block ticket")
    print("4 : Exit\n")

    ch = int(input("Enter any option: "))

    if ch == 1:
        hall_1.view_show_list()

    elif ch == 2:
        hall_1.view_available_seats()

    elif ch == 3:
        hall_1.book_seats()
    elif ch == 4:
        break


