import csv
import math

from Package import Package
from HashMap import HashMap
from Truck import Truck

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
        package_id=packageItem[0]
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

# load each package
load_packages()

# load trucks here

# method for delivering a  package
def deliver_pacakge(truck):

    # initially, no packages have been delivered, so place them in undelivered list
    undelivered=[]

    for package_id in truck.packages:
        package=package_hash_map.getValue(package_id)

        undelivered.append(package)

    # clear packages from truck, so we can reconstruct based on package with the shortest
    # distance first
    truck.packages.clear();

    while len(undelivered)>0:
        next_shortest_distance=math.inf;

        next_package=None;

        # keep delivering the packages that will require the shortest distance first
        for package in undelivered:
            if find_distance(get_address_index(package.address),get_address_index(
                    truck.address))<=next_shortest_distance:

                next_shortest_distance=find_distance(get_address_index(package.address),
                                                     get_address_index(truck.address))

                next_package=package







