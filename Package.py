class Package:
    def __init__(self,id,address,city,state,zip_code,delivery_deadline,weight,status):
        self.id = id
        self.address = address
        self.city = city
        self.state=state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.depart_time=None;
        self.delivery_time=None;

    def update_status(self,at_time):
        if at_time>=self.delivery_time:
            self.status = "Delivered"
        elif at_time>=self.depart_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"

    # must use strftime("%I:%M:%S %p") after datetime object to get the correct string version
    # where the hour will be displayed in a 12 hour formart and the correct AM/PM will be
    # appended
    def __str__(self):
        if self.status=="Delivered":
            return ("Id:%s, Address: %s, City: %s, State: %s, Zip Code: %s, Weight: "
                    "%s, "
                    "Delivery Deadline: %s, Status: %s, Depart Time: %s, Delivery Time: %s") % (
                self.id,
                                                                             self.address, self.city,
                                                           self.state, self.zip_code,
                                                           self.weight, self.delivery_deadline,
                                                            self.status,
                                                             self.depart_time.strftime("%I:%M:%S %p"),
                self.delivery_time.strftime("%I:%M:%S %p"))
        elif self.status=="En Route" or self.status== "At Hub":
            return ("Id:%s, Address: %s, City: %s, State: %s, Zip Code: %s, Weight: "
                    "%s, "
                    "Delivery Deadline: %s, Status: %s, Depart Time: %s") % (
                self.id,
                self.address, self.city,
                self.state, self.zip_code,
                self.weight, self.delivery_deadline,
                self.status,
                self.depart_time.strftime("%I:%M:%S %p"))
        return None



