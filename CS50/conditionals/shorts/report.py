"""
An example of how to use dictionaries in python
how to update dictionaries and integrate them into a report
"""

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft.update({"orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get["name", "unknown"]}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit {spacecraft.get("orbit", "unknown")}

    ==========================
    """

main()