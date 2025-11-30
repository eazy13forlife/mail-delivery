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

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                       self.state, self.zip_code,
                                                       self.delivery_deadline, self.weight,
                                                        self.status)
