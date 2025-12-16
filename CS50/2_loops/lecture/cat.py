"""
While Loops

We want to print "meow" 3 times without hard coding print("Meow") 3 times
"""
# i = 3
# while i != 0:
#     print("MEOW")
#     i = i - 1

"""
You can also use addition instead
"""
# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1

"""
Count from zero
"""
# i = 0 
# while i < 3:
#     print("meow")
#     i += 1 

# ========= For Loops ============

# for i in [0, 1, 2]:
#     print("meow")

# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="")

# ===========================

# while True:
#     n = int(input("What is your number? (n) "))
#     if n > 0:
#         break


def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What is your number(n)? "))
        if n > 0:
            return n
 
main()