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

    def __str__(self):

        return ("Id:%s, Address: %s, City: %s, State: %s, Zip Code: %s, Weight: "
                "%s, "
                "Delivery Deadline: %s, Status: %s, Depart Time: %s, Delivery Time: %s") % (
            self.id,
                                                                         self.address, self.city,
                                                       self.state, self.zip_code,
                                                       self.weight, self.delivery_deadline,
                                                        self.status,
                                                         self.depart_time,self.delivery_time)
