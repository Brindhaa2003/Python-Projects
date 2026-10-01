from abc import*
class BookMyShow(ABC):

    @abstractmethod
    def ticketBooking(self,no_of_seats):
        pass

    def discount(self,amount):
        print("5% discount")
        return amount*5/100
class srisakthi(BookMyShow):

    def __init__(self) -> None:
        self.available_seat=100

    def ticketBooking(self, no_of_seats):
        if no_of_seats<=self.available_seat:
            print("As per seat: Rs.150/-")
            bill=no_of_seats*150
            discount=super().discount(bill)
            payamt=bill-discount
            print("Bill Amount:",bill)
            print("Discount Amount:",discount)
            print("Payable Amount:",payamt)
            print("Ticket Booked Succesfully")
            self.available_seat-=no_of_seats
        else:
            print("Seats are not Available")

class Usha(BookMyShow):

    def __init__(self):
        self.available_seat=150
    
    def ticketBooking(self, no_of_seats):
       
        if no_of_seats<=self.available_seat:
            print("As per Seat: Rs.200/-")
            bill=no_of_seats*200
            discount=super().discount(bill)
            payamt=bill-discount
            print("Bill Amount:",bill)
            print("Discount Amount:",discount)
            print("Payable Amount:",payamt)
            print("Ticket Booked Succesfully")
            self.available_seat-=no_of_seats
        else:
            print("Seats are not Available")

class Devi(BookMyShow):
    def __init__(self):
        self.available_seat=120
    
    def ticketBooking(self, no_of_seats):
       
        if no_of_seats<=self.available_seat:
            print("As per Seat: Rs.180/-")
            bill=no_of_seats*180
            discount=super().discount(bill)
            payamt=bill-discount
            print("Bill Amount:",bill)
            print("Discount Amount:",discount)
            print("Payable Amount:",payamt)
            print("Ticket Booked Succesfully")
            self.available_seat-=no_of_seats
        else:
            print("Seats are not Available")

s=srisakthi()
u=Usha()
d=Devi()

while True:
    print("---Welcome to BookMy Show Ticket Booking Application---")
    print("Press 1.Ticket Booking")
    print("press 2.Exit")
    choice=int(input("Enter a Choice:"))
    if choice==1:
        no_of_seats=int(input("Enter a no.of.seats:"))
        print("press 1.SriSakthi Cinemas")
        print("press 2.Usha Cinemas")
        print("press 3.Devi Cinemas")
        cinema_option=int(input("Enter a Wanted Cinemas"))
        if cinema_option==1:
            print("----SriSakthi Cinemas----")
            print("---Available Movies in SriSakthi Cinemas---")
            print("1.Ayalaan")
            print("2.Goat")
            print("3.Bigil")
            s.ticketBooking(no_of_seats)
            break
        elif cinema_option==2:
            print("----Usha Cinemas----")
            print("---Available Movies in Usha Cinemas---")
            print("1.Gilli")
            print("2.Ratchasan")
            print("3.Vaalai")
            u.ticketBooking(no_of_seats)
            break
        elif cinema_option==3:
            print("---- Devi Cinemas----")
            print("---Available Movies in Devi Cinemas---")
            print("1.Ayalaan")
            print("2.Three")
            print("3.Nama Veetu Pillai")
            d.ticketBooking(no_of_seats)
            break
        else:
            print("Please Select a Valid Cinema")
    elif choice==2:
        print("Thank You..")
        break
    else:
        print("Invalid Choice")
    print("------------------------------------------")

