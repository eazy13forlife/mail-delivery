import csv
import datetime
import math

from Package import Package
from HashMap import HashMap
from Truck import Truck

# read all the csv files and creates lists from them
with open("CSV/Distances.csv") as csvfile:
    csv_distances = csv.reader(csvfile)
    distances_list = list(csv_distances)

with open("CSV/Packages.csv") as csvfile:
    csv_packages = csv.reader(csvfile)
    packages_list = list(csv_packages)


with open("CSV/Addresses.csv") as csvfile:
    csv_addresses = csv.reader(csvfile)
    addresses_list = list(csv_addresses)

# finds distance between two addresses, using the address_index
def find_distance(address_one_index,address_two_index):

    address_one_index = int(address_one_index)

    address_two_index = int(address_two_index)

    distance=distances_list[address_one_index][address_two_index]

    if distance=="":
        distance=distances_list[address_two_index][address_one_index]

    return float(distance)

# gets the index of an address from the address itself, so can be used in find_distance method
def get_address_index(address):
    for address_list in addresses_list:
        if address_list[2] == address:
            return address_list[0]

    return None

# create a hash map for packages
package_hash_map= HashMap()

# method for loading each package into hashmap
def load_packages():
    for packageItem in packages_list:
        package_id=int(packageItem[0])
        package_address=packageItem[1]
        package_city=packageItem[2]
        package_state=packageItem[3]
        package_zip_code=packageItem[4]
        package_delivery_deadline=packageItem[5]
        package_weight=packageItem[6]
        package_status="At hub"

        package=Package(package_id,package_address,package_city,package_state,package_zip_code,
                        package_delivery_deadline,package_weight,package_status)

        package_hash_map.insert(package_id,package)

# loads each package
load_packages()

# method for delivering a  package
def deliver_pacakge(truck):

    # initially, no packages have been delivered, so place them in undelivered list
    undelivered=[]

    for package_id in truck.packages:
        package=package_hash_map.get_value(package_id)

        undelivered.append(package)

    # clear packages from truck, so we can reconstruct based on package with the shortest
    # distance first
    truck.packages.clear();

    while len(undelivered)>0:
        next_shortest_distance=math.inf;

        next_package=None;

        # find the package that will require the shortest distance from where our truck
        # currently is
        for package in undelivered:
            if find_distance(get_address_index(package.address),get_address_index(
                    truck.address))<=next_shortest_distance:

                next_shortest_distance=find_distance(get_address_index(package.address),
                                                     get_address_index(truck.address))

                next_package=package
        # add the package to the truck packages, this is the next pacakge it will deliver
        truck.packages.append(next_package.id);

        # when did pacakge depart? same as the truck's initial departure time when leaving hub
        next_package.depart_time=truck.depart_time

        # total miles truck has gone since delivering this pacakge is current total miles +
        # distance of package
        truck.total_miles+=next_shortest_distance;

        # the new address of our truck is now at the address of where package was
        # delivered
        truck.address=next_package.address;

        # update the time after the truck delivers the package which is current time plus
        # time it takes to deliver the package so += m/mph
        truck.time+=datetime.timedelta(hours=next_shortest_distance/18)

        # the package that is delivered has the delivery time of when truck delivered the
        # package
        next_package.delivery_time=truck.time;

        next_package.status="Delivered"

        # remove the package from undelivered since truck has "delivered" it
        undelivered.remove(next_package)


# early morning deadline
truck1=Truck(16,0,[1,13,14,15, 16,19,20,29,30,31,34,37,40],"4001 South 700 East",0,datetime.timedelta(hours=8))

# eod mostly
truck3=Truck(16,0,[ 2, 4, 5, 7, 8,9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],"4001 South 700 East",0,datetime.timedelta(hours=10,minutes=20))

#only on truck 2 or eod
truck2=Truck(16,0,[3,6, 18, 25,28,32,36,38,27,35,39],"4001 South 700 East",0,datetime.timedelta(hours=9,minutes=5))


deliver_pacakge(truck1)
deliver_pacakge(truck3)
deliver_pacakge(truck2)
print(package_hash_map.get_value(25))
print(truck1.depart_time,truck1.time,truck1.total_miles)



