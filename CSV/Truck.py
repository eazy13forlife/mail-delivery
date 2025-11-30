class Truck:
    def __init__(self,max_capacity,current_capacity,packages,address,total_miles):
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.packages = packages
        self.address = address
        self.total_miles = total_miles

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.max_capacity,self.current_capacity,
                                               self.packages, self.address, self.total_miles);