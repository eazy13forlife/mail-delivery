class Truck:
    def __init__(self,max_capacity,current_capacity,packages,address,total_miles,depart_time):
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.packages = packages
        self.address = address
        self.total_miles = total_miles
        self.depart_time=depart_time
        self.time=depart_time


    def __str__(self):
        return ("Max Capacity: %s,Current Capacity: %s, Packages: %s, Address: %s, "
                "Total Miles: %s,"
                " Depart Time: %s,"
                "Time: %s") % (self.max_capacity,self.current_capacity,
                                               self.packages, self.address,
                                           self.total_miles,self.depart_time,self.time);