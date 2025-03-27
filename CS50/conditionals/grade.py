def main():
    score = int(input("Score: "))

    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score <= 89 and score >= 80:
        print("Grade: B")
    elif score <= 79 and score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")

main()