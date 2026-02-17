class Truck:
    def __init__(self,truck_number,max_capacity,current_capacity,packages,address,total_miles,
                 depart_time):
        self.truck_number = truck_number,
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.packages = packages
        self.address = address
        self.total_miles = total_miles
        self.depart_time=depart_time
        self.time=depart_time

    # must use strftime("%I:%M:%S %p") after datetime object to get the correct string version
    # where the hour will be displayed in a 12 hour formart and the correct AM/PM will be
    # appended
    def __str__(self):
        return ("Truck Number: %s, Max Capacity: %s,Current Capacity: %s, Packages: %s, "
                "Address: %s, "
                "Total Miles: %s,"
                " Depart Time: %s,"
                "Time: %s") % (self.truck_number,self.max_capacity,self.current_capacity,
                                               self.packages, self.address,
                                           self.total_miles,self.depart_time.strftime("%I:%M:%S %p"),self.time.strftime("%I:%M:%S %p"));