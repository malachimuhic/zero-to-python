def main():
    brickcolumn(4)
    printrow(4)
    print_square(4)

def brickcolumn(height):
    for _ in range(height):
        print("#")

def printrow(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)





main()