"""
This file goes over how to use lists in Python using append()
"""
results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.extend(["Bowser", "Donkey Kong Jr."])

results.remove("Bowser")
results.insert(0, "Bowser"  )




print(results)

