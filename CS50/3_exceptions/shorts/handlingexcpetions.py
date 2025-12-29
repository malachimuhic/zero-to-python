"""
An example of how to use dictionaries in python
how to use keys() method
"""

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU" ,
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not included in system")
        return
    except ValueError:
        print(f"Con't convert '{distances[spacecraft]}' to a float")
        return
     
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700 # distance of one AU in meters

main()