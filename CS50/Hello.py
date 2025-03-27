name = input("What is your name? ").strip().title()

#Split first and last name 
first, last = name.split(" ")

# Hello User
print(f"Hello {first}")

"""
Python print() Documentation
print(*objects, sep=' ', end='\n' file=sys.stdout, flush=False)
"""