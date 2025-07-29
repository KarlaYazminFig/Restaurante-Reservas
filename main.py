#Restaurant Reservations System
class Table:
    def __init__(self, num, capacity):
        self.num = num
        self.capacity = capacity
    
    def __str__(self):
        return f"Number: {self.num} | Capacity: {self.capacity}"
    
class Reservation:
    def __init__(self, table, customer_name):
        self.table = table
        self.customer_name = customer_name

    def __str__(self):
        return f"Table: {self.table} | Name: {self.customer_name}"
    
class Restaurant:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.list_reserved_tables = []
        self.list_available_tables = [1,2,3,4,5,6,7,8,9,10]
    
    def reserved_table(self, reservation):
        list_reserved = []
        for i in self.list_reserved_tables:
            list_reserved.append(i.table.num)

        num = int(reservation.table.num)

        if num > 0 and num < 11:
            if reservation.table.num not in list_reserved:
                self.list_reserved_tables.append(reservation)
                print(f"{reservation} | The table has been reserved ")
                for i in self.list_available_tables:
                    if i == num:
                        self.list_available_tables.remove(i) 
            else:
                print(f"Sorry, Table {reservation.table.num} is currently reserved")
        else:
            print("Right now, we only have 10 tables available to reserve")

    def cancel_reservation(self, reservation):
        found = False
        for i in self.list_reserved_tables:
            if i == reservation:
                found = True
                self.list_reserved_tables.remove(reservation)
                print(f"Reservation: {reservation} | has been removed")
                num = int(reservation.table.num)
                self.list_available_tables.append(num)
                self.list_available_tables.sort()
        if found == False:
            print(f"Reservation: {reservation} has not been found")

    def show_table_status(self):
        availables = []
        not_availables = []
        for i in self.list_available_tables:
            availables.append(i) 
        print("These tables are available to reserve: ")   
        print(availables)

        for i in self.list_reserved_tables:
            num = int(i.table.num)
            not_availables.append(num)
        print("These tables are actually reserved: ")  
        print(not_availables)

t1 = Table("2","4")
t2 = Table("2","4")
t3 = Table("3","2")
t4 = Table("15", "7")
reservation1 = Reservation(t1,"José Luis")
reservation2 = Reservation(t2,"Esther")
reservation3 = Reservation(t3,"Efren")
reservation4 = Reservation(t4, "María")
r1 = Restaurant("Sawpaoj","av.reforma N.1234", "9365106529")
r1.reserved_table(reservation1)
r1.reserved_table(reservation2)
r1.reserved_table(reservation3)
r1.cancel_reservation(reservation1)
r1.reserved_table(reservation4)
r1.show_table_status()