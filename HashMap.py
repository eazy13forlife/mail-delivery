class HashMap:
    def __init__(self,size=53):
       self.list=[]

       for i in range(size):
           self.list.append([])

# takes in a key and returns the value
    def get_value(self,key):

        bucket_index=hash(key)%len(self.list)

        bucket_list=self.list[bucket_index]

        # if key exists, just return the value
        for list_item in bucket_list:
            if list_item[0] == key:
                return list_item[1]

        # if no key exists, return None
        return None

    def get_all_values(self):
        all_values=[]

        for bucket_list in self.list:
            for list_item in bucket_list:
                all_values.append(list_item[1])

        return all_values

    def insert(self,key,value):
        bucket_index=hash(key)%len(self.list)

        bucket_list=self.list[bucket_index]

        # if key exists, just update key
        for list_item in bucket_list:
            if list_item[0] == key:
                list_item[1]=value
                return True

        #Otherwise just append this key,item to end of our bucket
        bucket_list.append([key,value])

        return True;

    def remove(self,key):
        bucket_index=hash(key)%len(self.list);

        bucket_list=self.list[bucket_index]

        value=self.get_value(key)

        if value is not None:
                 bucket_list.remove([key,value])
                 return True

        # if key doesn't exist, return false
        return False;





