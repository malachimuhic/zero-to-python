"""
How to use Tuples

what is the difference between tuple and list?

tuple cannot be added or subracted from and it is more effiecient (memory wise)
tuple = ()
list = []
"""

def main():
    coordinates = (42.376, -71.115)
    latitude, longitude = coordinates

    # print(f"Latitude: {coordinates[0]}")
    # print(f"Longitude: {coordinates[1]}")

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

main()