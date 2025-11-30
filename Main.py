import csv
from Package import Package
from HashMap import HashMap

with open("CSV/Distances.csv") as csvfile:
    csv_distances = csv.reader(csvfile)
    distances_list = list(csv_distances)

with open("CSV/Packages.csv") as csvfile:
    csv_packages = csv.reader(csvfile)
    packages_list = list(csv_packages)


with open("CSV/Addresses.csv") as csvfile:
    csv_addresses = csv.reader(csvfile)
    addresses_list = list(csv_addresses)

# load each package into hash table
package_hash_map= HashMap();

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
                    package_delivery_deadline,package_weight,package_status);

    package_hash_map.insert(package);


