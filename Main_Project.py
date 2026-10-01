from pymysql import*
class databasecode:
        
    def __init__(self):
        try:
            self.connection=connect(host="localhost",user="root",password="brindha",database="project")
        except Exception as e:
            print(e,"connection failed")
        else:
            print("connected")
            
    def __del__(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e,"Failed to close the connection")
        else:
            print("Connection Closed")
            
    def insert(self,sno,movie_name,ticket_price):
        try:
            query="insert into ticket values('{0}','{1}','{2}')".format(sno,movie_name,ticket_price)
            c=self.connection.cursor()
            result=c.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e,"Not Inserted")
        else:
            print("Inserted")
            
    def update(self,movie_name,ticket_price,sno):
        try:
            query="update ticket set movie_name='{0}',ticket_price='{1}' where sno='{2}'".format(movie_name,ticket_price,sno)
            c=self.connection.cursor()
            result=c.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e,"Failed to uodate")
        else:
            print("Updated Succesfully")
            
    def delete(self,sno):
        try:
            query="delete from ticket where sno='{0}'".format(sno)
            c=self.connection.cursor()
            result=c.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e,"failed to delete")
        else:
            print("Deleted Successfully")
            
    def view(self):
        try:
            query="select*from ticket"
            c=self.connection.cursor()
            result=c.execute(query)
            a=c.fetchall()
        except Exception as e:
            print(e,"Failed to view the Application")
        else:
            return a
        
    def login(self,username,password):
        try:
            query="select*from login where username='{0}' and password='{1}'".format(username,password)
            c=self.connection.cursor()
            result=c.execute(query)
            a=c.fetchall()
        except Exception as e:
            print(e)
        else:
            if len(a)!=0:
                return True
            else:
                return False
           
object=databasecode()
print("---Login Page---")
username=input("Enter the username:")
password=input("Enter the password:")
if object.login(username,password):
    while True:
        print("---Welcome to Ticket Booking Application---")
        print("1. Add Movies")
        print("2. Update Movies")
        print("3. delete Movies")
        print("4. View Available Movies")
        print("5. Exit")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            sno=int(input("Enter Serial No:"))
            movie_name=input("Enter Movie Name:")
            ticket_price=int(input("Enter Ticket Price:"))
            object.insert(sno,movie_name,ticket_price)
        elif choice==2:
            movie_name=input("Enter Movie Name:")
            ticket_price=int(input("Enter Ticket Price"))
            sno=int(input("Enter Serial No for update:"))
            object.update(movie_name,ticket_price,sno)
        elif choice==3:
            sno=int(input("Enter Serial no for delete:"))
            object.delete(sno)
        elif choice==4:
            print("Available Movies..")
            a=object.view()
            print("sno\t Movie_Name\t\t Price")
            for i in a:
                for j in i:
                    print(j,end="\t\t")
                print("")
            print("1.Ticket Booking")
            print("2.Exit")
            opt=int(input("Enter a Option:"))
            if opt==1:
                print("please select a wanted movie")
                sno=int(input("Enter a movie Sno:"))
                if sno==1:
                    print("Ayallan Movie")
                    print("As per Seat 160/-")
                    print("Bill Amount 160..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
                if sno==2:
                    print("Veeram Movie")
                    print("As per Seat 180/-")
                    print("Bill Amount 180..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
                if sno==3:
                    print("Goat Movie")
                    print("As per Seat 250/-")
                    print("Bill Amount 250..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
                if sno==4:
                    print("Beast Movie")
                    print("As per Seat 230/-")
                    print("Bill Amount 230..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
                if sno==5:
                    print("Amaran Movie")
                    print("As per Seat 340/-")
                    print("Bill Amount 340..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
                if sno==6:
                    print("Jailer Movie")
                    print("As per Seat 220/-")
                    print("Bill Amount 220..")
                    print("Proceed to pay...?")
                    print("1.yes 2.No")
                    pay=input("Enter a Choice for pay:")
                    if pay=='yes':
                        print("Ticket Booking...")
                        print("Ticket Booked Succesfully...")
                        print("Happy to Watching Movie")
                    else:
                        print("Thank you")
            else:
                print("Exit Succesfully")   
            
        elif choice==5:
            print("Thank you for using this application...")
            break
else:
    print("Invalid Login")
    print("Please Check the username and password")
        
            
            