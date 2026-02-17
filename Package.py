from datetime import datetime

class Package:
    def __init__(self,id,address,city,state,zip_code,truck_number,delivery_deadline,weight,
                 status):
        self.id = id
        self.address = address
        self.city = city
        self.state=state
        self.zip_code = zip_code
        self.truck_number=None;
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.depart_time=None;
        self.delivery_time=None;

    def update_status(self,at_time):
        if self.id == 9:
            if at_time < datetime.strptime("10:20:00 ""AM", "%I:%M:%S %p"):
                self.address = "300 State St"
            else:
                self.address = "410 S. State St"

        if at_time>=self.delivery_time:
            self.status = "Delivered"
        elif at_time>=self.depart_time:
            self.status = "En Route"
        elif at_time<self.depart_time:
            if self.id==6 or self.id==25 or self.id==28 or self.id==32:
                self.status = "Delayed on flight"
            else:
                self.status = "At Hub"


    # must use strftime("%I:%M:%S %p") after datetime object to get the correct string version
    # where the hour will be displayed in a 12 hour formart and the correct AM/PM will be
    # appended
    def __str__(self):
        if self.status=="Delivered":
            return ("Id:%s, Address: %s, City: %s, State: %s, Zip Code: %s, Weight: "
                    "%s, Truck Number: %s, "
                    "Delivery Deadline: %s, Status: %s, Depart Time: %s, Delivery Time: %s") % (
                self.id,
                                                                             self.address, self.city,
                                                           self.state, self.zip_code,
                                                           self.weight,
                self.truck_number, self.delivery_deadline,
                                                            self.status,
                                                             self.depart_time.strftime("%I:%M:%S %p"),
                self.delivery_time.strftime("%I:%M:%S %p"))
        elif self.status=="En Route" or self.status== "At Hub" or self.status== ("Delayed on "
                                                                                 "flight"):
            return ("Id:%s, Address: %s, City: %s, State: %s, Zip Code: %s, Weight: "
                    "%s,Truck Number: %s, "
                    "Delivery Deadline: %s, Status: %s, Depart Time: %s") % (
                self.id,
                self.address, self.city,
                self.state, self.zip_code,
                self.weight, self.truck_number, self.delivery_deadline,
                self.status,
                self.depart_time.strftime("%I:%M:%S %p"))
        return None



